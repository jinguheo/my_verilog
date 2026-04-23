package memoryrepo
import ("context"; "github.com/example/verilog-module-qa-api/internal/domain")
type versionRepo struct { items map[string][]domain.ModuleVersion }
func NewVersionRepository() domain.VersionRepository { return &versionRepo{items: map[string][]domain.ModuleVersion{"uart_rx":{{ModuleName:"uart_rx",VersionRef:"v1",CommitHash:"abc123",Summary:"initial imported version"},{ModuleName:"uart_rx",VersionRef:"v2",CommitHash:"def456",Summary:"timing cleanup and sampling fix"}}}} }
func (r *versionRepo) ListByModuleName(ctx context.Context, name string) ([]domain.ModuleVersion, error) { return r.items[name], nil }
