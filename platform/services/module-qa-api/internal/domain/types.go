package domain
type Module struct { Name string `json:"name"`; Summary string `json:"summary"`; Project string `json:"project"`; FilePath string `json:"file_path"`; Labels []string `json:"labels"`; Confidence float64 `json:"confidence"` }
type Connectivity struct { ModuleName string `json:"module_name"`; Parents []string `json:"parents"`; Children []string `json:"children"`; Ports []Port `json:"ports"`; Signals []string `json:"signals"` }
type Port struct { Name string `json:"name"`; Direction string `json:"direction"`; WidthExpr string `json:"width_expr,omitempty"` }
type ModuleVersion struct { ModuleName string `json:"module_name"`; VersionRef string `json:"version_ref"`; CommitHash string `json:"commit_hash,omitempty"`; Summary string `json:"summary,omitempty"` }
type SearchResult struct { Name string `json:"name"`; Summary string `json:"summary"`; Project string `json:"project"`; Labels []string `json:"labels"`; Confidence float64 `json:"confidence"` }
