       
registry_cfg = {
    "url" : "ghcr.io", 
    "user": "_put_username", 
    "token": "_put_token",
    "images_prefix": "ghcr.io/eflows4hpc/"
    }
    
repositories_cfg = {
    "workflow_repository":"/path/to/workflow-registry/",
    "software_repository":"/path/to/software-catalog/" 
    }

build_cfg = {
    "tmp_folder":"./", 
    "builder_home": "/tmp/image_creation/", 
    "base_image": "spack_base", 
    "dockerfile": "Dockerfile.spack", 
    "spack_cfg":"/tmp/software-catalog/cfg",
    "max_concurrent_builds" : 3,
    "singularity_sudo" : True
    }

database = 'sqlite:///db.sqlite'
port = 5000
host = '0.0.0.0'
application_root = 'image_creation'
secret_key = '_put_here_the_secret_key'
