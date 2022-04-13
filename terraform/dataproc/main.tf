provider "google" {
  project = var.project_id
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_storage_bucket" "ingestion-bucket" {
  location = "us-central1"
  name     = var.ingestion_bucket_name
}

resource "google_storage_bucket" "staging-bucket" {
  location = "us-central1"
  name     = var.staging_bucket_name
}

resource "google_dataproc_cluster" "spark-cluster" {
  name   = "my-cluster-1"
  region = "us-central1"

  cluster_config {
    staging_bucket = var.staging_bucket_name

    master_config {
      num_instances = var.master_num_instances
      machine_type  = "e2-medium"
      disk_config {
        boot_disk_type    = "pd-standard"
        boot_disk_size_gb = 30
      }
    }
    worker_config {
      num_instances = var.worker_num_instances
      machine_type  = "e2-medium"
      disk_config {
        boot_disk_type    = "pd-standard"
        boot_disk_size_gb = 30
      }
    }
    preemptible_worker_config {
      num_instances = 0
    }
  }
}