import nbformat

nb = nbformat.read('python_basics.ipynb', as_version=4)
errors = 0
executed = 0
for i, c in enumerate(nb.cells):
    if c.cell_type != 'code':
        continue
    executed += 1
    has_error = any(o.get('output_type') == 'error' for o in c.get('outputs', []))
    if has_error:
        errors += 1
        for o in c.get('outputs', []):
            if o.get('output_type') == 'error':
                print('Cell', i, '错误:', o.get('ename'), ':', o.get('evalue'))
print('代码单元数:', executed, '错误数:', errors)
print('全部通过!' if errors == 0 else '存在错误!')
