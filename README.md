Tracing tool for py. Copy paste into main. Trace. Have Fun!

# Hack Usage
```
import httpx
exec(httpx.get('https://raw.githubusercontent.com/ko10ok/ttpy/refs/heads/main/trace.py').text)

interceptor = FunctionInterceptor()
sys.settrace(interceptor.trace_calls)
```

## Default
interceptor = FunctionInterceptor()
sys.settrace(interceptor.trace_calls)

## Max
interceptor = FunctionInterceptor(include_file_fn=lambda filename: filename != '', min_time_ms=100)
sys.settrace(interceptor.trace_calls)

# Correct 
Copy https://raw.githubusercontent.com/ko10ok/ttpy/refs/heads/main/trace.py script
run 
```
interceptor = FunctionInterceptor()
sys.settrace(interceptor.trace_calls)
```
