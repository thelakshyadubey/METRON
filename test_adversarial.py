"""Quick test of adversarial framework"""

print("Testing imports...")
try:
    from adversarial_fixtures import (
        JAILBREAK_ATTACKS,
        PROMPT_INJECTION_ATTACKS,
        PII_EXTRACTION_ATTACKS,
        TOXIC_ATTACKS,
        SOCIAL_ENGINEERING_ATTACKS,
        ALL_BASELINE_ATTACKS,
        LEGACY_FORMAT_PERSONAS,
    )
    print("✅ adversarial_fixtures imported")
    print(f"   - Baseline attacks: {len(ALL_BASELINE_ATTACKS)}")
    print(f"   - Legacy personas: {len(LEGACY_FORMAT_PERSONAS)}")
except Exception as e:
    print(f"❌ adversarial_fixtures failed: {e}")
    exit(1)

try:
    from adversarial_generator import (
        generate_attack_mutations,
        evaluate_response_with_rubric,
        expand_attack_suite,
        batch_evaluate_responses,
        generate_compliance_report,
        MUTATION_TECHNIQUES,
    )
    print("✅ adversarial_generator imported")
    print(f"   - Mutation techniques: {len(MUTATION_TECHNIQUES)}")
    print(f"   - Techniques: {list(MUTATION_TECHNIQUES.keys())[:3]}...")
except Exception as e:
    print(f"❌ adversarial_generator failed: {e}")
    exit(1)

print("\nAll imports successful! ✨")
print("\nExample attack:")
print(f"  ID: {JAILBREAK_ATTACKS[0]['id']}")
print(f"  Severity: {JAILBREAK_ATTACKS[0]['severity']}")
print(f"  Prompt: {JAILBREAK_ATTACKS[0]['prompt'][:60]}...")
print(f"  Compliance: {', '.join(JAILBREAK_ATTACKS[0]['compliance_tags'])}")
