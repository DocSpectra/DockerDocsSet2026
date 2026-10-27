{{ define "left" }} {{- partial "sidebar/mainnav.html" . }}

Filter guides by tag or programming language.

Tags {{- range $name, $data := hugo.Data.tags }} {{- if where $.Pages "Params.tags" "intersect" (slice $name) }} {{- $id := anchorize (fmt.Printf "tag-%s" $name) }} {{ $data.title }} {{- end }} {{ end }} Languages {{- range $name, $data := hugo.Data.languages }} {{- if where $.Pages "Params.languages" "intersect" (slice $name) }} {{- $id := anchorize (fmt.Printf "lang-%s" $name) }} {{ $data.title }} {{- end }} {{ end }} {{ end }} {{ define "main" }} {{- partial "breadcrumbs.html" . }}

# {{ .Title }}

{{ .Content }}

## Featured guides

{{- $featured := where .Pages "Params.featured" true }} {{- with $featured }} {{- range . }} [{{- $img := resources.Get (.Params.image | default "/images/thumbnail.webp") }}]({{ .Permalink }})

[{{ .Title }}]({{ .Permalink }})

{{ .Summary }}

{{ template "guide-metadata" . }} {{- end }} {{- end }}

## All guides

{{ partialCached "icon" "filter_alt" "filter_alt" }}

Filtered results: showing out of guides.

{{- range $name, $data := hugo.Data.tags }} {{ template "termchip" $data.title }} {{- end }} {{- range $name, $data := hugo.Data.languages }} {{ $data.title }} {{- end }} {{- range .Pages }} [{{ .Title }}]({{ .Permalink }}) {{ template "guide-metadata" . }} {{- end }} {{ end }} {{- define "guide-metadata" }} {{- with .Params.languages }} {{ partial "guide-languages.html" . }} {{- end }} {{- with .Params.tags }} {{ partial "guide-tags.html" . }} {{- end }} {{- with .Params.time }} {{ partialCached "icon" "schedule" "schedule" }} {{ . }} {{- end }} {{- end }} {{- define "termchip" }} {{ partialCached "icon" "tag" "tag" }} {{ . }} {{- end }}
