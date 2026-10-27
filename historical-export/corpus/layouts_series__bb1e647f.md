{{ define "article" }} {{ partial "breadcrumbs.html" . }}

# {{ .Title }}

{{ partialCached "pagemeta.html" . . }} {{ .Summary }} {{- if or .Params.proficiencyLevel .Params.time .Params.prerequisites }} {{- with .Params.proficiencyLevel }} Skill level {{ . }} {{- end }} {{- with .Params.time }} Time to complete {{ . }} {{- end }} {{- with .Params.prerequisites }} Prerequisites {{ . }} {{- end }} {{- end }} {{ .Content }} {{ partial "heading.html" (dict "text" "Modules" "level" 2) }} {{- range .Pages }}

- [{{ .LinkTitle }}]({{ .Permalink }})

{{ plainify .Description }}

{{- end }} {{ end }} {{ define "right" }}{{ end }}
