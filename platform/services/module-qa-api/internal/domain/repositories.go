package domain
import "context"
type ModuleRepository interface { Search(ctx context.Context, q string) ([]SearchResult, error); GetByName(ctx context.Context, name string) (*Module, error) }
type ConnectivityRepository interface { GetByModuleName(ctx context.Context, name string) (*Connectivity, error) }
type VersionRepository interface { ListByModuleName(ctx context.Context, name string) ([]ModuleVersion, error) }
