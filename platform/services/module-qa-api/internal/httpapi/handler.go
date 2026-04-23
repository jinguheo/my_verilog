package httpapi
import ("encoding/json"; "net/http"; "strings"; "github.com/example/verilog-module-qa-api/internal/app")
type Handler struct { svc *app.Service }
func NewHandler(svc *app.Service) *Handler { return &Handler{svc:svc} }
func (h *Handler) Routes() http.Handler {
	mux:=http.NewServeMux()
	mux.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request){ writeJSON(w,http.StatusOK,map[string]any{"service":"module-qa-api","status":"ok"}) })
	mux.HandleFunc("/api/v1/modules/search", func(w http.ResponseWriter, r *http.Request){ q:=r.URL.Query().Get("q"); results,_:=h.svc.SearchModules(r.Context(), q); writeJSON(w,http.StatusOK,map[string]any{"query":q,"results":results}) })
	mux.HandleFunc("/api/v1/modules/", h.handleModuleRoutes)
	return mux
}
func (h *Handler) handleModuleRoutes(w http.ResponseWriter, r *http.Request) {
	path:=strings.Trim(strings.TrimPrefix(r.URL.Path,"/api/v1/modules/"),"/")
	if path=="" { writeJSON(w,http.StatusBadRequest,map[string]any{"error":"missing module name"}); return }
	parts:=strings.Split(path,"/"); name:=parts[0]
	if len(parts)==1 { m,err:=h.svc.GetModule(r.Context(),name); if err!=nil { writeJSON(w,http.StatusNotFound,map[string]any{"error":err.Error()}); return }; writeJSON(w,http.StatusOK,m); return }
	switch parts[1] {
	case "connectivity": c,err:=h.svc.GetConnectivity(r.Context(),name); if err!=nil { writeJSON(w,http.StatusNotFound,map[string]any{"error":err.Error()}); return }; writeJSON(w,http.StatusOK,c)
	case "versions": v,_:=h.svc.GetVersions(r.Context(),name); writeJSON(w,http.StatusOK,map[string]any{"module_name":name,"versions":v})
	default: writeJSON(w,http.StatusNotFound,map[string]any{"error":"route not found"})
	}
}
func writeJSON(w http.ResponseWriter, status int, v any) { w.Header().Set("Content-Type","application/json"); w.WriteHeader(status); _=json.NewEncoder(w).Encode(v) }
