terraform {
  required_version = ">=0.13.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
backend "s3" {
    bucket = "exz1"
    key = "terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "exz1-lockID"

  }
}

# Configure the AWS provider
provider "aws" {
  region     = "us-east-1"
}

resource "aws_security_group" "app" {
  name        = "app"
  description = "security group"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

 ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags= {
    Name = "web_app"
  }
}

resource "aws_instance" "web_instance" {
  ami           = "ami-0866a3c8686eaeeba"
  instance_type = "t3.micro"
  security_groups = ["web_app"]

  user_data = <<-EOF
  #!/bin/bash
  curl -fsSL https://get.docker.com -o get-docker.sh
  sudo sh get-docker.sh
  sudo groupadd docker
  sudo usermod -aG docker $USER
  newgrp docker
  docker pull  andriypolyuh/exz:latest
  docker run -it andriypolyuh/exz:latest

  EOF


  tags = {
    Name = "webapp_instance"
  }
}


output "instance_public_ip" {
  value     = aws_instance.web_instance.public_ip
  sensitive = true
}
