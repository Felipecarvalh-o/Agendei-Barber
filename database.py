from supabase import create_client
import uuid

# ================= CONFIG =================
SUPABASE_URL = "https://xclixjztgjlbwndrumed.supabase.co"
SUPABASE_KEY = "sb_publishable_dYoF_Sr-yBc8dyxZofXCaA_fjOofLaQ"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ============================================================
# ======================= AUTH ===============================
# ============================================================

def login_email(email, password):
    """Login tradicional por email/senha"""
    try:
        res = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        return res.user
    except Exception as e:
        print("Erro login:", e)
        return None


def login_social(provider):
    """Login OAuth (Google / Apple)"""
    try:
        res = supabase.auth.sign_in_with_oauth({
            "provider": provider,
            "options": {"redirect_to": "http://localhost:8501"}
        })
        return res.url
    except Exception as e:
        print("Erro login social:", e)
        return None


# ============================================================
# ===================== PERFIS ===============================
# ============================================================

def get_or_create_profile(user_id, email, default_role="client"):
    """
    Retorna SEMPRE um profile válido.
    Se não existir → cria automaticamente.
    """

    try:
        res = (
            supabase
            .table("profiles")
            .select("*")
            .eq("id", user_id)
            .execute()
        )

        # SE O PERFIL EXISTE
        if res.data:
            return res.data[0]

        # SE NÃO EXISTE → CRIAR
        new_profile = {
            "id": user_id,
            "email": email,
            "name": "",
            "phone": "",
            "role": default_role,        # barber ou client → vem do start.py
            "barbershop_name": None
        }

        insert_res = supabase.table("profiles").insert(new_profile).execute()

        return insert_res.data[0] if insert_res.data else new_profile

    except Exception as e:
        print("Erro ao buscar ou criar profile:", e)

        return {
            "id": user_id,
            "email": email,
            "name": "",
            "phone": "",
            "role": default_role,
            "barbershop_name": None
        }


# ============================================================
# ==================== CLIENTES ==============================
# ============================================================

def listar_clientes():
    """Lista todos os clientes cadastrados"""
    try:
        res = (
            supabase
            .table("profiles")
            .select("*")
            .eq("role", "client")
            .order("name")
            .execute()
        )
        return res.data or []
    except Exception as e:
        print("Erro listar clientes:", e)
        return []


def criar_cliente(nome, telefone=None):
    """Criação manual de cliente"""
    try:
        novo = {
            "id": str(uuid.uuid4()),
            "role": "client",
            "name": nome,
            "phone": telefone
        }
        supabase.table("profiles").insert(novo).execute()

    except Exception as e:
        print("Erro criar cliente:", e)


# ============================================================
# ==================== SERVIÇOS ==============================
# ============================================================

def listar_servicos(barbeiro_id):
    try:
        res = (
            supabase
            .table("services")
            .select("*")
            .eq("barber_id", barbeiro_id)
            .order("name")
            .execute()
        )
        return res.data or []
    except Exception as e:
        print("Erro listar serviços:", e)
        return []


def criar_servico(barbeiro_id, nome, preco, duracao):
    try:
        novo = {
            "id": str(uuid.uuid4()),
            "barber_id": barber_id,
            "name": nome,
            "price": preco,
            "duration_minutes": duracao
        }
        supabase.table("services").insert(novo).execute()

    except Exception as e:
        print("Erro criar serviço:", e)


# ============================================================
# ==================== AGENDA ================================
# ============================================================

def listar_agendamentos(barbeiro_id):
    """Retorna agendamentos + JOIN cliente e serviço"""
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
            .order("appointment_time")
            .execute()
        )
        return res.data or []
    except Exception as e:
        print("Erro listar agendamentos:", e)
        return []


def criar_agendamento(barbeiro_id, client_id, service_id, data_hora):
    try:
        novo = {
            "id": str(uuid.uuid4()),
            "barber_id": barber_id,
            "client_id": client_id,
            "service_id": service_id,
            "appointment_time": data_hora
        }

        supabase.table("appointments").insert(novo).execute()

    except Exception as e:
        print("Erro criar agendamento:", e)


# ============================================================
# ==================== LEMBRETES =============================
# ============================================================

def criar_lembrete(appointment_id, canal="whatsapp"):
    try:
        novo = {
            "id": str(uuid.uuid4()),
            "appointment_id": appointment_id,
            "channel": canal
        }
        supabase.table("reminders").insert(novo).execute()

    except Exception as e:
        print("Erro criar lembrete:", e)


def listar_lembretes():
    try:
        res = supabase.table("reminders").select("*").execute()
        return res.data or []
    except Exception as e:
        print("Erro listar lembretes:", e)
        return []
