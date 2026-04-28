import re
from datetime import datetime
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    # 🔥 IMPORTANTE: headless=True para que funcione en GitHub Actions
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    print("🚀 Navegando al formulario...")
    page.goto("https://forms.office.com/pages/responsepage.aspx?id=4ZwiXzx37Uam-pdABvrglxZYPNAMWcNDpeoPSnrcguVUREhDRFYyQVY4SDlCRE0xSE9TNDU5SkZJSi4u&route=shorturl")
    
    print("📝 Llenando el formulario...")
    page.get_by_role("radio", name="EPIROC").check()
    page.get_by_role("textbox", name="2. Reportado por:Respuesta").fill("Ever Abraham Medrano Silva")
    page.get_by_role("textbox", name="3. N° DE CONTRATORespuesta").fill("37032401264")
    page.get_by_role("radio", name="Turno A").check()

    # Fecha actual
    today_str = datetime.now().strftime("%d/%m/%Y")
    print(f"📅 Insertando fecha: {today_str}")

    page.get_by_role("combobox", name="FechaRespuesta necesaria").click()
    page.get_by_role("combobox", name="FechaRespuesta necesaria").click()
    page.get_by_role("combobox", name="FechaRespuesta necesaria").fill(today_str)

    page.get_by_role("textbox", name="6. Número de Personas -").click()
    page.get_by_role("textbox", name="6. Número de Personas -").fill("2")
    page.get_by_role("textbox", name="7. Número de Personas -").fill("1")
    page.get_by_role("textbox", name="8. Número de Personas -").fill("0")
    page.get_by_role("textbox", name="9. Número de Personas -").fill("0")

    # Si quieres enviar el formulario, descomenta la siguiente línea
    # print("📤 Enviando formulario...")
    # page.get_by_role("button", name="Enviar").click()
    
    print("✅ Formulario llenado exitosamente!")
    
    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
