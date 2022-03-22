{{/*
define global labels helm chart
*/}}
{{- define "chart.labels" -}}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
calculated variables
*/}}

{{- define "app.fullName" -}}
helm-{{ .Values.projectName }}-{{ .Values.applicationName }}
{{- end -}}

{{- define "app.image" -}}
{{ .Values.images.app.registry }}/{{ .Values.images.app.imageName }}
{{- end -}}

{{/*
Create chart name and version as used by the chart label
*/}}
{{- define "app.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | lower }}
{{- end -}}

