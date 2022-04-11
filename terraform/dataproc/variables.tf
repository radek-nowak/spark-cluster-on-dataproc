variable "project_id" {
  description = "Id of the GCP project."
  type        = string
  default     = ""
}

variable "staging_bucket_name" {
  description = "The name of GCS bucket used for staging"
  type        = string
  default     = ""
}

variable "master_num_instances" {
  description = "The number of master node instances"
  type        = number
  default     = 1
}

variable "worker_num_instances" {
  description = "The number of master node instances"
  type        = number
  default     = 2
}