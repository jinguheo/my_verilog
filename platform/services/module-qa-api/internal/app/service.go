package app
import ("context"; "errors"; "github.com/example/verilog-module-qa-api/internal/domain")
var ErrNotFound = errors.New("not found")
type Service struct { modules domain.ModuleRepository; connectivity domain.ConnectivityRepository; versions domain.VersionRepository }
func NewService(m domain.ModuleRepository, c domain.ConnectivityRepository, v domain.VersionRepository) *Service { return &Service{modules:m, connectivity:c, versions:v} }
func (s *Service) SearchModules(ctx context.Context, q string) ([]domain.SearchResult, error) { return s.modules.Search(ctx, q) }
func (s *Service) GetModule(ctx context.Context, name string) (*domain.Module, error) { m,err:=s.modules.GetByName(ctx,name); if err!=nil {return nil,err}; if m==nil {return nil,ErrNotFound}; return m,nil }
func (s *Service) GetConnectivity(ctx context.Context, name string) (*domain.Connectivity, error) { c,err:=s.connectivity.GetByModuleName(ctx,name); if err!=nil {return nil,err}; if c==nil {return nil,ErrNotFound}; return c,nil }
func (s *Service) GetVersions(ctx context.Context, name string) ([]domain.ModuleVersion, error) { return s.versions.ListByModuleName(ctx, name) }
