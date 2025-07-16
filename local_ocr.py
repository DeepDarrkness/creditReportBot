import pymupdf4llm
import time

start_conversion = time.perf_counter()
md_text = pymupdf4llm.to_markdown("./pdf/dinesh.pdf")
end_conversion = time.perf_counter()

print (f"Conversion took {end_conversion - start_conversion} seconds")
print (md_text)