Tracing tool for py. Copy paste into main. Trace. Have Fun!

# Hack Usage
```python
# README https://github.com/ko10ok/ttpy
import httpx
exec(httpx.get('https://raw.githubusercontent.com/ko10ok/ttpy/refs/heads/main/trace.py').text)

interceptor = FunctionInterceptor()
sys.settrace(interceptor.trace_calls)
```

## Default
```python
interceptor = FunctionInterceptor()
sys.settrace(interceptor.trace_calls)
```

## Max
```python
interceptor = FunctionInterceptor(include_file_fn=lambda filename: filename != '', min_time_ms=100)
sys.settrace(interceptor.trace_calls)
```

# Correct 
Copy https://raw.githubusercontent.com/ko10ok/ttpy/refs/heads/main/trace.py script
run 
```
interceptor = FunctionInterceptor()
sys.settrace(interceptor.trace_calls)
```
