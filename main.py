from servicedesk_api import create_access_token, list_tickets, export_tickets

if __name__ == "__main__":
    try:
        print("🔐 Gerando token de acesso...")
        token = create_access_token()
        print("✅ Token obtido.\n")

        print("📥 Buscando chamados...")
        tickets = list_tickets(token, limite=50)
        print(f"✅ Total de chamados: {len(tickets)}")

        print("💾 Exportando para arquivos JSON...")
        export_tickets(tickets)

        print(
            "🏁 Processo concluído. Agora importe o arquivo JSON manualmente no Zoho Analytics."
        )

    except Exception as e:
        print(f"❌ Erro: {e}")
