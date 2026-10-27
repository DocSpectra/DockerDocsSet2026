{{ define "article" }} {{ partial "breadcrumbs.html" . }} {{ with .Title }}

# {{ . }}

{{ end }} {{ with .Content }} {{ . }} {{ end }} Term Definition {{ range $term, $definition := hugo.Data.glossary }} {{ $term }} {{ $definition | $.RenderString }} {{ end }} {{ end }}
