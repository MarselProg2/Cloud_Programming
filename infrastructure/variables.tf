variable "project_name" {
  description = "Präfix für alle Azure-Ressourcen. Muss global eindeutig im Storage-Account-Namen sein."
  type        = string
  default     = "helloworld"
}

variable "location" {
  description = "Azure-Region für die Bereitstellung"
  type        = string
  default     = "West Europe"
}
