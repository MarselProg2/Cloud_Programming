output "static_website_url" {
  description = "Öffentliche URL der deployten Hello-World-Seite"
  value       = azurerm_storage_account.web.primary_web_endpoint
}

output "storage_account_name" {
  description = "Name des Azure Storage Accounts"
  value       = azurerm_storage_account.web.name
}
