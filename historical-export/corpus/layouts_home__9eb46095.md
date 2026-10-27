{{ partial "head.html" . }} {{ partial "header.html" . }} {{ partial "gordon-chat.html" . }}

# How can we help?

{{ partialCached "icon" "icons/gordon.svg" "icons/gordon.svg" }} {{ partialCached "icon" "icons/gordon-happy.svg" "icons/gordon-happy.svg" }} {{ partialCached "icon" "arrow_forward" "arrow_forward" }} {{ range slice "How do I get started with Docker?" "Can I run my AI agent in a sandbox?" "What is a container?" "What are Docker Hardened Images?" "Why should I use Docker Compose?" }} {{ . }} {{ end }} {{ range slice (dict "url" "/get-started/" "icon" "rocket" "title" "Get started" "description" "Learn Docker basics.") (dict "url" "/guides/" "icon" "menu_book" "title" "Guides" "description" "Optimize your development workflows with Docker.") (dict "url" "/manuals/" "icon" "description" "title" "Manuals" "description" "Install, set up, configure, and use Docker products.") (dict "url" "/reference/" "icon" "terminal" "title" "Reference" "description" "Browse the CLI and API documentation.") }} [{{ partialCached "icon" .icon .icon }}]({{ .url }})

### [{{ .title }}]({{ .url }})

[{{ .description }}]({{ .url }})

{{ end }}

## Featured topics

{{ range slice (dict "url" "/dhi/" "title" "Docker Hardened Images") (dict "url" "/ai/sandboxes/get-started/" "title" "Get started with Docker Sandboxes") (dict "url" "/desktop/" "title" "Docker Desktop overview") (dict "url" "/engine/install/" "title" "Install Docker Engine") (dict "url" "/reference/dockerfile/" "title" "Dockerfile reference") (dict "url" "/build/" "title" "Docker Build overview") }} [{{ .title }}]({{ .url }}) [{{ partialCached "icon" "arrow_forward" "arrow_forward" }}]({{ .url }}) {{ end }}
