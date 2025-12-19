from supabase import create_client

# ================= CONFIG =================
SUPABASE_URL = "https://xclixjztgjlbwndrumed.supabase.co"
SUPABASE_KEY = "sb_publishable_dYoF_Sr-yBc8dyxZofXCaA_fjOofLaQ"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# ================= AUTH =================
def login_email(email, password):
    try:
        res = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        return res.user
    except Exception as e:
        print("Erro no login:", e)
        return None


# ================= PROFILE =================
def get_or_create_profile(user_id, email):
    """
    Garante que SEMPRE retorna um profile válido.
    Nunca retorna None.
    """
    try:
        # Buscar perfil
        res = (
            supabase
            .table("profiles")
            .select("*")
            .eq("id", user_id)
            .execute()
        )

        # Já existe
        if res.data:
            return res.data[0]

        # Criar perfil novo
        new_profile = {
            "id": user_id,
            "email": email,
            "name": "",
            "phone": "",
            "role": "barber"
        }

        insert_res = supabase.table("profiles").insert(new_profile).execute()

        # Garantir retorno mesmo sem data (às vezes supabase não retorna)
        return insert_res.data[0] if insert_res.data else new_profile

    except Exception as e:
        print("Erro ao buscar ou criar profile:", e)

        # Nunca deixa o app quebrar
        return {
            "id": user_id,
            "email": email,
            "name": "",
            "phone": "",
            "role": "barber"
        }


# ================= CLIENTES =================
def listar_clientes():
    try:
        res = (
            supabase
            .table("profiles")
            .select("*")
            .eq("role", "client")
            .order("name", desc=False)
            .execute()
        )
        return res.data or []
    except Exception as e:
        print("Erro ao listar clientes:", e)
        return []


def criar_cliente(nome, telefone=None):
    try:
        novo_cliente = {
            "role": "client",
            "name": nome,
            "phone": telefone
        }
        supabase.table("profiles").insert(novo_cliente).execute()
    except Exception as e:
        print("Erro ao criar cliente:", e)


# ================= SERVIÇOS =================
def listar_servicos(barbeiro_id):
    try:
        res = (
            supabase
            .table("services")
            .select("*")
            .eq("barber_id", barbeiro_id)
            .order("name", desc=False)
            .execute()
        )
        return res.data or []
    except Exception as e:
        print("Erro ao listar serviços:", e)
        return []


def criar_servico(barbeiro_id, nome, preco, duracao):
    try:
        supabase.table("services").insert({
            "barber_id": barbeiro_id,
            "name": nome,
            "price": preco,
            "duration_minutes": duracao
        }).execute()
    except Exception as e:
        print("Erro ao criar serviço:", e)


# ================= AGENDA =================
def listar_agendamentos(barbeiro_id):
    try:
        res = (
            supabase
            .table("appointments")
            .select("""
                *,
                client:profiles(name, phone),
                service:services(name, duration_minutes, price)
            """)
            .eq("barber_id", barbeiro_id)
            .order("appointment_time", desc=False)
            .execute()
        )
        return res.data or []
    except Exception as e:
        print("Erro ao listar agendamentos:", e)
        return []


def criar_agendamento(barbeiro_id, client_id, service_id, data_hora):
    try:
        supabase.table("appointments").insert({
            "barber_id": barbeiro_id,
            "client_id": client_id,
            "service_id": service_id,
            "appointment_time": data_hora
        }).execute()
    except Exception as e:
        print("Erro ao criar agendamento:", e)


# ================= LEMBRETES =================
def criar_lembrete(appointment_id, canal="whatsapp"):
    try:
        supabase.table("reminders").insert({
            "appointment_id": appointment_id,
            "channel": canal
        }).execute()
    except Exception as e:
        print("Erro ao criar lembrete:", e)


def listar_lembretes():
    try:
        res = supabase.table("reminders").select("*").execute()
        return res.data or []
    except Exception as e:
        print("Erro ao listar lembretes:", e)
        return []
