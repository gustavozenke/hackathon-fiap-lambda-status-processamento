variable "function_name" {
  type        = string
  default     = "hackathon-status-processamento"
}

variable "function_role" {
  type        = string
  default     = "arn:aws:iam::369780787289:role/LabRole"
}

variable "handler" {
  type        = string
  default     = "application.entrypoint.lambda_handler.lambda_handler"
}

variable "runtime" {
  type        = string
  default     = "python3.9"
}

variable "timeout" {
  type        = number
  default     = 60
}