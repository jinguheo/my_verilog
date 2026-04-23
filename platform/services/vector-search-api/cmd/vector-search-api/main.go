package main
import ("log"; "net/http"; "os"; "github.com/example/vector-search-api/internal/httpapi")
func main(){ addr:=getenv("HTTP_ADDR",":8090"); h:=httpapi.NewHandler(); log.Printf("vector-search-api listening on %s", addr); log.Fatal(http.ListenAndServe(addr, h.Routes())) }
func getenv(k, fallback string) string { if v:=os.Getenv(k); v!="" { return v }; return fallback }
