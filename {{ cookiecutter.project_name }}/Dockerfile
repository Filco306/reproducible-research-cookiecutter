{%- if (cookiecutter.language == "python3" and cookiecutter.gpu_usage== "no") -%}
{%- include 'Dockerfiles/Dockerfile_python3' %}
    {%- if cookiecutter.framework_if_using_python=="pytorch" -%}
    {%- include 'Dockerfiles/Dockerfile_pytorch' %}
    {%- elif cookiecutter.framework_if_using_python=="tensorflow" -%}
    {%- include 'Dockerfiles/Dockerfile_tensorflow' %}
    {%- endif -%}
{%- elif ((cookiecutter.language == "python3" and cookiecutter.gpu_usage== "yes") and cookiecutter.CUDA_version=="9.0") -%}
{%- include 'Dockerfiles/Dockerfile_python3_cuda9' %}

{%- endif -%}
