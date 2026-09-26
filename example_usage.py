import sys, json
from client import VoiceTurnTakingEndpointDetector

def main():
    print("Testing VoiceTurnTakingEndpointDetector...")
    detector = VoiceTurnTakingEndpointDetector()
    results = detector.run_benchmark_turn_detection()
    print(json.dumps(results, indent=2))
    assert results["scenario_active_speech"] == "CONTINUE_LISTENING", "Failed active speech test"
    assert results["scenario_hesitation"] == "HOLD_BACKCHANNEL", "Failed hesitation test"
    assert results["scenario_endpoint_detected"] == "ENDPOINT_DETECTED", "Failed endpoint test"
    print("All Voice Turn Taking Endpoint Detector tests passed successfully!")

if __name__ == "__main__":
    main()
