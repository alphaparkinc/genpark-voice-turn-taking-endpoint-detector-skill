import sys, json
from client import VoiceTurnTakingEndpointDetector

def main():
    detector = VoiceTurnTakingEndpointDetector()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(detector.run_benchmark_turn_detection(), indent=2))
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            method = req.get("method")
            params = req.get("params", {})
            rid = req.get("id")

            if method == "tools/list":
                res = {
                    "tools": [
                        {"name": "analyze_turn_status", "description": "Evaluate multi-modal turn endpointing from acoustic energy and trailing transcript."},
                        {"name": "calibrate_acoustic_thresholds", "description": "Calibrate background noise floor and silence threshold adaptively."},
                        {"name": "predict_semantic_closure", "description": "Compute semantic sentence completion likelihood and trailing connective score."},
                        {"name": "run_benchmark_turn_detection", "description": "Execute deterministic turn-taking endpointing test scenarios."}
                    ]
                }
            elif method == "tools/call":
                tname = params.get("name")
                args = params.get("arguments", {})
                if tname == "analyze_turn_status":
                    out = detector.analyze_turn_status(args.get("frame_energies_db", []), args.get("transcript_fragment", ""), args.get("elapsed_silence_ms", 0))
                elif tname == "calibrate_acoustic_thresholds":
                    out = detector.calibrate_acoustic_thresholds(args.get("ambient_frames_db", []))
                elif tname == "predict_semantic_closure":
                    out = detector.predict_semantic_closure(args.get("transcript_fragment", ""))
                elif tname == "run_benchmark_turn_detection":
                    out = detector.run_benchmark_turn_detection()
                else:
                    out = {"error": f"Unknown tool {tname}"}
                res = {"content": [{"type": "text", "text": json.dumps(out)}]}
            else:
                res = {"error": "Unsupported method"}
            print(json.dumps({"jsonrpc": "2.0", "id": rid, "result": res}), flush=True)
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}), flush=True)

if __name__ == "__main__":
    main()
