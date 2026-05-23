DROP TABLE IF EXISTS rtl_parser_lsp;
CREATE TABLE rtl_parser_lsp (
  name text,
  project text,
  path text,
  path_file text,
  ports text,
  instances text,
  instance_names text,
  labels text,
  summary text,
  parents text
) morphology='stem_en' min_infix_len='2';

-- Example query:
-- SELECT id, WEIGHT(), name, project FROM rtl_parser_lsp
-- WHERE MATCH('@name ibex_alu | @ports operand_a_i | @instances prim_fifo_sync')
-- ORDER BY WEIGHT() DESC LIMIT 5;
