# Konzeptionelle Überlegungen: Hello World in der Cloud

## 1. Ausgangslage und Zielsetzung

Die Aufgabe verlangt eine einfache „Hello-World"-Webseite, die ohne vertiefte Webprogrammierkenntnisse umsetzbar ist. Zentrales Lernziel ist nicht die Entwicklung komplexer Anwendungslogik, sondern das Verständnis für Cloud-Infrastrukturen und deren modellierbare, reproduzierbare Bereitstellung mittels Infrastructure as Code (IaC). Ziel ist es, die Seite kostengünstig, wartungsarm und skalierbar in einer Public Cloud zu betreiben.

## 2. Wahl des Cloud-Anbieters und der Dienste

Als Cloud-Anbieter wurde **Microsoft Azure** gewählt. Azure bietet mit dem **Azure Storage Account** ein verwaltetes Dienst, das über das integrierte „Static Website"-Feature das Hosten von rein clientseitigen HTML-Seiten ohne eigenen Webserver ermöglicht. Dies reduziert Betriebsaufwand und Kosten erheblich, da keine virtuellen Maschinen, Container oder App Services laufen müssen. Die Alternative AWS mit S3 und CloudFront ist ebenfalls denkbar; für eine rein statische Einstiegsseite ist Azure Storage aber besonders einfach zu konfigurieren und direkt im Azure-Portal sowie per Terraform steuerbar.

## 3. Architektur und Datenfluss

Die Architektur besteht aus drei logischen Ebenen:

1. **Nutzer/Browser**: Stellt einen HTTPS-Request an die öffentliche Endpunkt-URL des Storage Accounts.
2. **Azure Storage Account mit Static Website**: Empfängt den Request und liefert aus dem Container `$web` die konfigurierte Startdatei `index.html` aus.
3. **Terraform (IaC)**: Beschreibt die gewünschte Infrastruktur, erzeugt die Ressourcen und lädt die HTML-Datei in den Storage-Container.

Der Datenfluss ist somit linear und transparent: Terraform provisioniert Ressource Group, Storage Account und Blob; der Nutzer ruft die automatisch generierte URL auf und erhält die Hello-World-Seite zurück. Ein optionales CDN (Azure CDN) könnte für globale Latenzoptimierung ergänzt werden, ist für diese einfache Aufgabe aber nicht erforderlich.

## 4. Infrastructure as Code mit Terraform

Terraform wurde als IaC-Tool gewählt, weil es anbieterunabhängig, deklarativ und weit verbreitet ist. Der Code legt in `main.tf`, `variables.tf` und `outputs.tf` fest, welche Ressourcen existieren sollen. Durch `terraform plan` und `terraform apply` wird die Infrastruktur reproduzierbar aufgebaut; `terraform destroy` ermöglicht ein vollständiges Aufräumen. Variablen wie `project_name` und `location` machen das Setup portabel zwischen Regionen oder Projekten.

## 5. Sicherheit und Kosten

Der Storage Account nutzt HTTPS, und das Static-Website-Feature stellt ausschließlich lesenden Zugriff auf den `$web`-Container bereit. Durch den Tarif „Standard" mit lokal redundanter Speicherung (LRS) entstehen nur sehr geringe Kosten, die sich auf wenige Cent pro Monat belaufen. Ein Schreibzugriff auf den Blob erfolgt ausschließlich über das Deployment von Terraform.

## 6. Fazit

Das Konzept zeigt, dass selbst ein einfaches Hello-World-Beispiel im Cloud-Kontext wertvolle Prinzipien vermittelt: Automatisierung über IaC, Nutzung verwalteter Cloud-Dienste, klare Ressourcenabgrenzung und ein nachvollziehbarer Datenfluss. Die gewählte Architektur ist minimal, erweiterbar und eignet sich als Grundlage für komplexere Cloud-Anwendungen.
