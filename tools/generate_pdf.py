"""Generiert die PDF-Abgabe (Konzeptionstext + Architekturdiagramm) im A4-Format."""
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(64, 64, 64)
        self.cell(0, 10, "Cloud Programming – Phase 1: Hello World in Azure", ln=True, align="C")
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Seite {self.page_no()}", align="C")


pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()
pdf.set_margins(20, 20, 20)

# Titel
pdf.set_font("Helvetica", "B", 16)
pdf.set_text_color(0, 120, 212)
pdf.cell(0, 12, "Konzeptionelle Überlegungen: Hello World in der Cloud", ln=True)
pdf.ln(4)

# Fließtext
pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(0, 0, 0)

text_sections = [
    (
        "1. Ausgangslage und Zielsetzung",
        "Die Aufgabe verlangt eine einfache \u201eHello-World\u201c-Webseite. Zentrales Lernziel ist nicht die Entwicklung komplexer Anwendungslogik, sondern das Verständnis für Cloud-Infrastrukturen und deren modellierbare, reproduzierbare Bereitstellung mittels Infrastructure as Code (IaC). Ziel ist es, die Seite kostengünstig, wartungsarm und skalierbar in einer Public Cloud zu betreiben."
    ),
    (
        "2. Wahl des Cloud-Anbieters und der Dienste",
        "Als Cloud-Anbieter wurde Microsoft Azure gewählt. Azure bietet mit dem Azure Storage Account ein verwaltetes Dienst, das über das integrierte \u201eStatic Website\u201c-Feature das Hosten von rein clientseitigen HTML-Seiten ohne eigenen Webserver ermöglicht. Dies reduziert Betriebsaufwand und Kosten erheblich. Für eine rein statische Einstiegsseite ist Azure Storage besonders einfach zu konfigurieren und direkt per Terraform steuerbar."
    ),
    (
        "3. Architektur und Datenfluss",
        "Die Architektur besteht aus drei Ebenen: (1) Nutzer/Browser stellt einen HTTPS-Request an die öffentliche Endpunkt-URL des Storage Accounts. (2) Azure Storage Account mit Static Website empfängt den Request und liefert aus dem Container $web die Startdatei index.html aus. (3) Terraform (IaC) beschreibt die gewünschte Infrastruktur, erzeugt die Ressourcen und lädt die HTML-Datei in den Storage-Container."
    ),
    (
        "4. Infrastructure as Code mit Terraform",
        "Terraform wurde als IaC-Tool gewählt, weil es anbieterunabhängig, deklarativ und weit verbreitet ist. Der Code legt in main.tf, variables.tf und outputs.tf fest, welche Ressourcen existieren sollen. Durch terraform plan und terraform apply wird die Infrastruktur reproduzierbar aufgebaut; terraform destroy ermöglicht ein vollständiges Aufräumen."
    ),
    (
        "5. Sicherheit und Kosten",
        "Der Storage Account nutzt HTTPS, und das Static-Website-Feature stellt ausschließlich lesenden Zugriff auf den $web-Container bereit. Durch den Tarif \u201eStandard\u201c mit lokal redundanter Speicherung (LRS) entstehen nur sehr geringe Kosten. Schreibzugriff erfolgt ausschließlich über das Terraform-Deployment."
    ),
    (
        "6. Fazit",
        "Das Konzept zeigt, dass selbst ein einfaches Hello-World-Beispiel im Cloud-Kontext wertvolle Prinzipien vermittelt: Automatisierung über IaC, Nutzung verwalteter Cloud-Dienste, klare Ressourcenabgrenzung und ein nachvollziehbarer Datenfluss."
    ),
]

for heading, body in text_sections:
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 7, heading, ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 5.5, body)
    pdf.ln(2)

# Architekturdiagramm zeichnen
pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 10, "Cloud-Architekturdiagramm", ln=True)

# Startposition für das Diagramm
start_y = pdf.get_y()
pdf.set_xy(20, start_y)

# Farben
blue = (0, 120, 212)
light_blue = (225, 243, 255)
green = (130, 179, 102)
light_green = (213, 232, 212)
yellow = (214, 182, 86)
light_yellow = (255, 242, 204)
orange = (215, 155, 0)
light_orange = (255, 230, 204)
grey = (102, 102, 102)
light_grey = (245, 245, 245)

# Boxen
box_h = 18
pdf.set_fill_color(*light_blue)
pdf.set_draw_color(*blue)
pdf.rect(20, start_y, 170, 80, style="DF")

# Resource Group Label
pdf.set_font("Helvetica", "I", 9)
pdf.set_text_color(*blue)
pdf.set_xy(22, start_y + 3)
pdf.cell(0, 5, "Azure Resource Group", ln=True)

# Terraform-IaC Box
pdf.set_fill_color(*light_grey)
pdf.set_draw_color(*grey)
pdf.rect(130, start_y + 15, 55, box_h, style="DF")
pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(130, start_y + 17)
pdf.multi_cell(55, 5, "Terraform\n(IaC)", align="C")

# Storage Account Box
pdf.set_fill_color(*light_yellow)
pdf.set_draw_color(*yellow)
pdf.rect(60, start_y + 15, 60, box_h, style="DF")
pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(60, start_y + 17)
pdf.multi_cell(60, 5, "Azure Storage Account\n(Static Website)", align="C")

# $web Container Box
pdf.set_fill_color(*light_green)
pdf.set_draw_color(*green)
pdf.rect(70, start_y + 50, 55, box_h, style="DF")
pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(70, start_y + 52)
pdf.multi_cell(55, 5, "$web-Container\n(öffentlich)", align="C")

# index.html File Box
pdf.set_fill_color(*light_orange)
pdf.set_draw_color(*orange)
pdf.rect(140, start_y + 50, 45, box_h, style="DF")
pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(140, start_y + 52)
pdf.multi_cell(45, 5, "index.html\n(Hello World)", align="C")

# Nutzer/Aktor (Kreis)
pdf.set_draw_color(0, 0, 0)
pdf.set_fill_color(248, 249, 250)
pdf.ellipse(35, start_y + 22, 12, 12, style="DF")
pdf.set_font("Helvetica", "B", 8)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(30, start_y + 36)
pdf.cell(25, 5, "Nutzer", align="C")

# Pfeile zeichnen (dünne Linien)
pdf.set_draw_color(*blue)
pdf.set_line_width(0.5)

# Nutzer -> Storage Account
pdf.line(47, start_y + 28, 60, start_y + 24)
# Pfeilspitze
pdf.line(57, start_y + 22, 60, start_y + 24)
pdf.line(57, start_y + 26, 60, start_y + 24)

# Storage Account -> $web
pdf.line(90, start_y + 33, 97, start_y + 50)
# Pfeilspitze
pdf.line(95, start_y + 46, 97, start_y + 50)
pdf.line(99, start_y + 46, 97, start_y + 50)

# Terraform -> $web (gestrichelt)
pdf.set_draw_color(*grey)
pdf.set_line_width(0.4)
# Mehrere kleine Segmente für gestrichelte Linie
segments = [(157, start_y + 33), (157, start_y + 42), (125, start_y + 42), (125, start_y + 50)]
for i in range(len(segments) - 1):
    pdf.line(segments[i][0], segments[i][1], segments[i + 1][0], segments[i + 1][1])
# Pfeilspitze
pdf.line(123, start_y + 46, 125, start_y + 50)
pdf.line(127, start_y + 46, 125, start_y + 50)

# index.html -> $web
pdf.set_draw_color(*orange)
pdf.set_line_width(0.4)
pdf.line(140, start_y + 59, 125, start_y + 59)
# Pfeilspitze
pdf.line(128, start_y + 57, 125, start_y + 59)
pdf.line(128, start_y + 61, 125, start_y + 59)

# $web -> Nutzer (Antwort)
pdf.set_draw_color(*blue)
pdf.set_line_width(0.5)
pdf.line(70, start_y + 59, 47, start_y + 59)
pdf.line(50, start_y + 57, 47, start_y + 59)
pdf.line(50, start_y + 61, 47, start_y + 59)

# Beschriftungen der Pfeile
pdf.set_font("Helvetica", "I", 7)
pdf.set_text_color(0, 0, 0)
pdf.set_xy(45, start_y + 17)
pdf.cell(0, 5, "HTTPS-Request")
pdf.set_xy(55, start_y + 63)
pdf.cell(0, 5, "HTML-Antwort")
pdf.set_xy(140, start_y + 42)
pdf.cell(0, 5, "Erzeugt & konfiguriert")
pdf.set_xy(108, start_y + 55)
pdf.cell(0, 5, "Upload")

pdf.ln(5)

# Hinweis
pdf.set_font("Helvetica", "I", 8)
pdf.set_text_color(100, 100, 100)
pdf.multi_cell(0, 4, "Hinweis: Das zugehörige editierbare Diagramm liegt als cloud-architecture.drawio vor und kann in draw.io weiterbearbeitet werden.")

out_path = "../Nachname-Vorname_Matrikelnummer_Kurs_P1_A.pdf"
pdf.output(out_path)
print(f"PDF erzeugt: {out_path}")
