package main
import (
	"log"
	"net/http"
	"os"
	"github.com/example/verilog-module-qa-api/internal/adapters/memoryrepo"
	"github.com/example/verilog-module-qa-api/internal/app"
	"github.com/example/verilog-module-qa-api/internal/httpapi"
)
func main() {
	addr := getenv("HTTP_ADDR", ":8088")
	svc := app.NewService(memoryrepo.NewModuleRepository(), memoryrepo.NewConnectivityRepository(), memoryrepo.NewVersionRepository())
	handler := httpapi.NewHandler(svc)
	log.Printf("module-qa-api listening on %s", addr)
	log.Fatal(http.ListenAndServe(addr, handler.Routes()))
}
func getenv(k, fallback string) string { if v:=os.Getenv(k); v!="" { return v }; return fallback }
