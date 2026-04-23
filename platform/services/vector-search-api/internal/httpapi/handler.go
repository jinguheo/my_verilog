package httpapi
import ("encoding/json"; "net/http")
type Handler struct{}
func NewHandler()*Handler{ return &Handler{} }
func (h *Handler) Routes() http.Handler {
	mux:=http.NewServeMux()
	mux.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request){ _=json.NewEncoder(w).Encode(map[string]any{"service":"vector-search-api","status":"ok"}) })
	mux.HandleFunc("/api/v1/semantic/search", func(w http.ResponseWriter, r *http.Request){ _=json.NewEncoder(w).Encode(map[string]any{"mode":"ontology-aware-semantic-search","results":[]map[string]any{{"name":"uart_rx","project":"opentitan","labels":[]string{"uart","approved"},"score":0.91}}}) })
	return mux
}
