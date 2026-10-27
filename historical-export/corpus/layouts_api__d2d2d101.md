# {{ printf "%s | %s" .Title site.Title }}

{{ $specURL := urls.Parse (printf "/%s%s.yaml" .File.Dir .File.ContentBaseName) }} {{ printf "%s | %s" .Title site.Title }} {{ partial "schema.html" . }}

# {{ .Title }}

{{ .Description }}

- [Open Markdown]({{ partial )

- [Download OpenAPI specification]({{ $specURL.String | absURL }})

{{ if or (strings.HasPrefix .RelPermalink "/reference/api/hub/") (strings.HasPrefix .RelPermalink "/reference/api/registry/") }} {{ else }} {{ end }}
