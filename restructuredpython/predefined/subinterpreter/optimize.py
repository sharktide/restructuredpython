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

import gc
import time
import sys
import functools
import multiprocessing
import warnings


def optimize_loop(
        profile=False,
        gct=False,
        multithreading=False,
        parallel=False,
        cache=False,
        unroll=0):
    """
    Decorator to optimize loop-like functions.
    Supports profiling, garbage collection, parallel execution, caching, and JIT compilation.
    """
    def decorator(fn):
        original_fn = fn

        # Caching
        if cache:
            fn = functools.lru_cache(maxsize=None)(fn)

        @functools.wraps(original_fn)
        def wrapper(*args, **kwargs):
            if gct:
                gc.collect()

            start = time.perf_counter() if profile else None

            fn(*args, **kwargs)

            if profile:
                duration = time.perf_counter() - start  # type: ignore
                print(f"[PROFILE] Loop took {duration:.4f}s")

        return wrapper
    return decorator


def optimize_function(profile=False, trace=False, cache=False, parallel=False):
    """
    Decorator to optimize general functions.
    Supports profiling, tracing, caching
    """
    def decorator(fn):
        original_fn = fn

        if cache:
            fn = functools.lru_cache(maxsize=None)(fn)

        if profile:
            @functools.wraps(original_fn)
            def profiled(*args, **kwargs):
                start = time.perf_counter()
                result = fn(*args, **kwargs)  # type: ignore
                print(
                    f"[PROFILE] {
                        original_fn.__name__} took {
                        time.perf_counter() -
                        start:.4f}s")
                return result
            return profiled

        if trace:
            def tracer(frame, event, arg):
                print(f"[TRACE] {event} in {frame.f_code.co_name}")
                return tracer

            @functools.wraps(original_fn)
            def traced(*args, **kwargs):
                sys.settrace(tracer)
                result = fn(*args, **kwargs)  # type: ignore
                sys.settrace(None)
                return result
            return traced

        return fn

    return decorator
