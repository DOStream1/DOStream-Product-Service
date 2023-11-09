import argparse
import requests

def upload_trivy_report(defectdojo_url, api_token, scan_data, trivy_report_path):
    headers = {
        "Authorization": f"Token {api_token}",
    }

    files = {
        "file": ("trivy-results.json", open(trivy_report_path, "rb"), "application/json")
    }

    response = requests.post(
        f"{defectdojo_url}/import-scan/",
        headers=headers,
        data=scan_data,
        files=files
    )

    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content.decode('utf-8')}")
    if response.status_code == 201:
        print("Trivy report uploaded successfully.")
    else:
        print("Failed to upload Trivy report.")

def main():
    parser = argparse.ArgumentParser(description="Upload Trivy report to DefectDojo")
    parser.add_argument("--defectdojo-url", type=str, required=True)
    parser.add_argument("--api-token", type=str, required=True)
    parser.add_argument("--minimum-severity", type=str, default="Info")
    parser.add_argument("--active", type=str, default="true")
    parser.add_argument("--verified", type=str, default="true")
    parser.add_argument("--scan-type", type=str, default="Trivy Scan")
    parser.add_argument("--close-old-findings", type=str, default="false")
    parser.add_argument("--push-to-jira", type=str, default="false")
    parser.add_argument("--product-name", type=str, default="Website")
    parser.add_argument("--scan-date", type=str, default="2022-06-14")
    parser.add_argument("--engagement-name", type=str, default="Gitlab-test1")
    parser.add_argument("--trivy-report-path", type=str, required=True)
    args = parser.parse_args()

    scan_data = {
        "minimum_severity": args.minimum_severity,
        "active": args.active,
        "verified": args.verified,
        "scan_type": args.scan_type,
        "close_old_findings": args.close_old_findings,
        "push_to_jira": args.push_to_jira,
        "product_name": args.product_name,
        "scan_date": args.scan_date,
        "engagement_name": args.engagement_name
    }

    upload_trivy_report(args.defectdojo_url, args.api_token, scan_data, args.trivy_report_path)

if __name__ == "__main__":
    main()


