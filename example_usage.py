import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import VisualGroundingSpecComparisonClient

def main():
    client = VisualGroundingSpecComparisonClient()
    res = client.compare_visual_specs()
    print("=== Visual Grounding Spec Comparison Output ===")
    print(f"Comparison: {res['compared_products'][0]} vs {res['compared_products'][1]}")
    print("\nSpec Delta Matrix:")
    for s in res['spec_delta_matrix']:
        print(f"  - {s['dimension']:<28}: {s['prod_a']} vs {s['prod_b']} -> Best: {s['advantage']}")
    print(f"\nRecommendation: {res['visual_recommendation']}")

if __name__ == '__main__':
    main()
