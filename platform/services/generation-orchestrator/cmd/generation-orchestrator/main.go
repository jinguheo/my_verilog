package main
import ("encoding/json"; "log"; "net/http"; "os")
func main(){ addr:=getenv("HTTP_ADDR",":8091"); http.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request){ _=json.NewEncoder(w).Encode(map[string]any{"service":"generation-orchestrator","status":"ok"}) }); http.HandleFunc("/api/v1/generate/plan", func(w http.ResponseWriter, r *http.Request){ _=json.NewEncoder(w).Encode(map[string]any{"priority":"ontology-first","steps":[]string{"parse structured spec","retrieve approved reference modules","build architecture plan","emit rtl skeleton"}}) }); log.Printf("generation-orchestrator listening on %s", addr); log.Fatal(http.ListenAndServe(addr,nil)) }
func getenv(k, fallback string) string { if v:=os.Getenv(k); v!="" { return v }; return fallback }
