rm -rf py_stubs

shopt -s globstar
for f in stubs/**/*.pyi; do 
    mkdir -p py_`dirname $f` && cp -- "$f" "py_${f%.pyi}.py"
done

