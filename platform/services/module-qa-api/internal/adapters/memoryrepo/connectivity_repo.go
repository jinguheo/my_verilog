package memoryrepo
import ("context"; "github.com/example/verilog-module-qa-api/internal/domain")
type connectivityRepo struct { items map[string]domain.Connectivity }
func NewConnectivityRepository() domain.ConnectivityRepository { return &connectivityRepo{items: map[string]domain.Connectivity{"uart_rx":{ModuleName:"uart_rx",Parents:[]string{"uart_core","top_earlgrey"},Children:[]string{},Ports:[]domain.Port{{Name:"clk_i",Direction:"input"},{Name:"rst_ni",Direction:"input"},{Name:"rx_i",Direction:"input"},{Name:"data_o",Direction:"output",WidthExpr:"8"}},Signals:[]string{"clk_i","rst_ni","rx_i","data_o"}}}} }
func (r *connectivityRepo) GetByModuleName(ctx context.Context, name string) (*domain.Connectivity, error) { item,ok:=r.items[name]; if !ok { return nil,nil }; cp:=item; return &cp,nil }
