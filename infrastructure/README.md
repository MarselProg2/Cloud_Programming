# Terraform-Infrastruktur: Hello World in Azure

Dieses Verzeichnis enthält den Infrastructure-as-Code-Teil für die Aufgabe.
Es wird ein Azure Storage Account mit aktiviertem Static-Website-Feature bereitgestellt und die `index.html` in den öffentlichen `$web`-Container geladen.

## Voraussetzungen

- [Terraform](https://www.terraform.io/downloads.html) installiert
- Azure CLI installiert und mit `az login` angemeldet
- Ein Azure-Abonnement

## Deployment

```bash
cd infrastructure
terraform init
terraform plan
terraform apply
```

Nach dem Deployment gibt Terraform die URL der statischen Website aus (z. B. `https://helloworldwebstor.z1.web.core.windows.net/`).

## Aufräumen

```bash
terraform destroy
```
