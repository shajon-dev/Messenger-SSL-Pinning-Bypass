# https://tools.shajon.dev/curl-converter | By SHAJON-404

import requests
import json

url = 'https://b-graph.facebook.com/graphql'

headers = {
    "x-fb-request-analytics-tags": json.dumps({
        "network_tags": {
            "product": "256002347743983",
            "request_category": "graphql",
            "purpose": "none",
            "retry_attempt": "0",
        },
        "application_tags": "graphservice",
    }, separators=(',', ':')),
    "x-fb-rmd": "state=URL_ELIGIBLE",
    "priority": "u=3, i",
    "user-agent": "Dalvik/2.1.0 (Linux; U; Android 14; TECNO CK7n Build/UP1A.231005.007) [FBAN/Orca-Android;FBAV/573.0.0.7.88;FBPN/com.facebook.orca;FBLC/en_US;FBBV/1029456948;FBCR/null;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO CK7n;FBSV/14;FBCA/arm64-v8a:null;FBDM/{density=2.7250001,width=1080,height=2292};FB_FW/1;]",
    "x-graphql-client-library": "graphservice",
    "content-type": "application/x-www-form-urlencoded",
    "x-zero-eh": "664c0faaac849cb891d0a261fbb72a12",
    "authorization": "OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
    "x-zero-state": "unknown",
    "x-zero-f-device-id": "e8ea88fd-1ddc-4ea5-8e8b-e63b7e1c8018",
    "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
    "x-fb-integrity-machine-id": "uhTcaVgbvTH1CBLbrEHXxoeH",
    "app-scope-id-header": "9b165b7d-d570-4f41-b8a2-af50214ce696",
    "x-fb-connection-type": "WIFI",
    "x-tigon-is-retry": "False",
    "x-fb-http-engine": "Tigon/Liger",
    "x-fb-client-ip": "True",
    "x-fb-server-cluster": "True",
    "x-fb-conn-uuid-client": "2gYrj7sNkvx2dQTkOgpzhQ==",
}

data = {
    "method": "post",
    "format": "json",
    "server_timestamps": "true",
    "locale": "en_US",
    "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
    "fb_api_caller_class": "graphservice",
    "client_doc_id": "11994080426029509508908565382",
    "fb_api_client_context": json.dumps({
        "is_background": False,
    }, separators=(',', ':')),
    "variables": json.dumps({
        "params": {
            "params": json.dumps({
                "params": json.dumps({
                    "client_input_params": {
                        "blocked_uids": [],
                        "aac": json.dumps({
                            "aac_init_timestamp": 1785679529,
                            "aacjid": "face0f87-5b16-4f28-be99-1367c70fdcb5",
                            "aaccs": "GT0gxQcNo-tU0haOkmM_6KXXcoo4IyJYdS9sSIBITvI",
                        }, separators=(',', ':')),
                        "sim_phones": [
                            "",
                        ],
                        "aymh_accounts": [],
                        "network_bssid": None,
                        "secure_family_device_id": "da8f76c2-095e-4f51-a746-1f8ed11100ae",
                        "attestation_result": {
                            "keyHash": "5c1914f53dba8cf1cec9de45c04d3ca1136f3a103c9dc80be16631a61c3b2c93",
                            "data": "eyJjaGFsbGVuZ2Vfbm9uY2UiOiJad3BiamVBb1lsYnNmNTJPaEhFbjdqSzFEUFdCUzBxTGExWFQwNDFOWXhNPSIsInVzZXJuYW1lIjoieDEuIHNoYWpvbiJ9",
                            "signature": "MEYCIQDzKK6gtdg1u4fkRBYLQIo0I3I4Ay3rb5urqaUrEbzg6wIhAKE0Qp4B+8oDr3DZd2pwOQrWmyaXTj7G+Ui6S1ue9lg+",
                        },
                        "has_granted_read_contacts_permissions": 0,
                        "auth_secure_device_id": "",
                        "has_whatsapp_installed": 1,
                        "password": "#PWD_MSGR:0:1785680183:ejkejwnsnsn",
                        "sso_token_map_json_string": "",
                        "block_store_machine_id": "",
                        "cloud_trust_token": None,
                        "event_flow": "login_manual",
                        "password_contains_non_ascii": "false",
                        "client_known_key_hash": "",
                        "sso_accounts_auth_data": [],
                        "encrypted_msisdn": "",
                        "has_granted_read_phone_permissions": 0,
                        "app_manager_id": "",
                        "should_show_nested_nta_from_aymh": 0,
                        "device_id": "9b165b7d-d570-4f41-b8a2-af50214ce696",
                        "zero_balance_state": "",
                        "login_attempt_count": 1,
                        "machine_id": "uhTcaVgbvTH1CBLbrEHXxoeH",
                        "accounts_list": [],
                        "gms_incoming_call_retriever_eligibility": "client_not_supported",
                        "family_device_id": "e8ea88fd-1ddc-4ea5-8e8b-e63b7e1c8018",
                        "fb_ig_device_id": [],
                        "device_emails": [],
                        "try_num": 1,
                        "lois_settings": {
                            "lois_token": "",
                        },
                        "event_step": "home_page",
                        "headers_infra_flow_id": "",
                        "openid_tokens": {},
                        "contact_point": "x1. shajon",
                    },
                    "server_params": {
                        "should_trigger_override_login_2fa_action": 0,
                        "is_from_logged_out": 0,
                        "should_trigger_override_login_success_action": 0,
                        "login_credential_type": "none",
                        "server_login_source": "login",
                        "waterfall_id": "53f0368b-2b70-4650-a6cf-bc563255b15c",
                        "two_step_login_type": "one_step_login",
                        "login_source": "Login",
                        "is_platform_login": 0,
                        "pw_encryption_try_count": 1,
                        "login_entry_point": "logged_out",
                        "INTERNAL__latency_qpl_marker_id": 36707139,
                        "is_from_aymh": 0,
                        "offline_experiment_group": "caa_iteration_v3_perf_msg_6",
                        "is_from_landing_page": 0,
                        "left_nav_button_action": "NONE",
                        "password_text_input_id": "vhj27c:103",
                        "is_from_empty_password": 0,
                        "is_from_msplit_fallback": 0,
                        "ar_event_source": "login_home_page",
                        "username_text_input_id": "vhj27c:102",
                        "layered_homepage_experiment_group": None,
                        "device_id": "9b165b7d-d570-4f41-b8a2-af50214ce696",
                        "login_surface": "login_home",
                        "INTERNAL__latency_qpl_instance_id": 190389424800587,
                        "reg_flow_source": "login_home_native_integration_point",
                        "is_caa_perf_enabled": 1,
                        "credential_type": "password",
                        "is_from_password_entry_page": 0,
                        "caller": "gslr",
                        "family_device_id": "e8ea88fd-1ddc-4ea5-8e8b-e63b7e1c8018",
                        "is_from_assistive_id": 0,
                        "access_flow_version": "pre_mt_behavior",
                        "is_from_logged_in_switcher": 0,
                    },
                }, separators=(',', ':')),
            }, separators=(',', ':')),
            "bloks_versioning_id": "d842120187a8cd1cc91e081fec802f4ff3399d41c589fd9c94f25d4ef66f3c35",
            "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request",
        },
        "scale": "3",
        "nt_context": {
            "theme_params": [
                {
                    "value": [
                        "three_neutral_gray",
                    ],
                    "design_system_name": "XMDS",
                },
                {
                    "value": [],
                    "design_system_name": "FDS",
                },
            ],
            "is_flipper_enabled": False,
            "android_device_performance_class": 0,
            "gpu_memory_mb": 7655,
            "debug_tooling_metadata_token": None,
            "android_os_api_level": 34,
        },
    }, separators=(',', ':')),
    "fb_api_analytics_tags": json.dumps([
        "GraphServices",
    ], separators=(',', ':')),
    "client_trace_id": "6e3f617f-08f3-486b-afd0-d83fb49c99e1",
}

response = requests.post(url, headers=headers, data=data)
print(f"Response Status Code: {response.status_code}")
print(f"Response Body: {response.text}")