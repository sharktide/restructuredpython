# Copyright 2025 Rihaan Meher

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gc, time, sys, functools, types, dis, multiprocessing

def optimize_loop(profile=False, gct=False, parallel=False, unroll=0):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            # Garbage Collection
            if gct:
                gc.collect()

            # Profiling
            start = time.perf_counter() if profile else None

            # Execute loop
            if parallel:
                # Naive parallelism: assuming fn yields or returns a list
                results = fn(*args, **kwargs)
                with multiprocessing.Pool() as pool:
                    pool.map(lambda x: x, results)
            else:
                fn(*args, **kwargs)

            if profile:
                duration = time.perf_counter() - start
                print(f"[PROFILE] Loop took {duration:.4f}s")

        return wrapper
    return decorator

def optimize_function(profile=False, trace=False):
    def decorator(fn):
        if profile:
            @functools.wraps(fn)
            def profiled(*args, **kwargs):
                start = time.perf_counter()
                result = fn(*args, **kwargs)
                print(f"[PROFILE] {fn.__name__} took {time.perf_counter() - start:.4f}s")
                return result
            return profiled
        if trace:
            def tracer(frame, event, arg):
                print(f"[TRACE] {event} in {frame.f_code.co_name}")
                return tracer
            def wrapped(*args, **kwargs):
                sys.settrace(tracer)
                result = fn(*args, **kwargs)
                sys.settrace(None)
                return result
            return wrapped
        return fn
    return decorator
