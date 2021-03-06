import pytest


SLE_11_SP4_BASE = [
    'SLE11-SDK-SP4-Pool',
    'SLE11-SDK-SP4-Updates',
    'SLE11-SP4-Debuginfo-Pool',
    'SLE11-SP4-Debuginfo-Updates',
    'SLES11-SP4-Pool',
    'SLES11-SP4-Updates'
]

SLE_11_SP4_MODULES = [
    'SLE11-Public-Cloud-Module',
    'SLE11-Security-Module',
    'SLES11-Extras'
]

SLE_12_BASE = [
    'SLES12-Debuginfo-Pool',
    'SLES12-Debuginfo-Updates',
    'SLES12-Pool',
    'SLES12-Updates',
    'SLE-SDK12-Debuginfo-Pool',
    'SLE-SDK12-Debuginfo-Updates',
    'SLE-SDK12-Pool',
    'SLE-SDK12-Updates'
]

SLE_12_MODULES = [
    'SLE-Module-Adv-Systems-Management12-Debuginfo-Pool',
    'SLE-Module-Adv-Systems-Management12-Debuginfo-Updates',
    'SLE-Module-Adv-Systems-Management12-Pool',
    'SLE-Module-Adv-Systems-Management12-Updates',
    'SLE-Module-Containers12-Debuginfo-Pool',
    'SLE-Module-Containers12-Debuginfo-Updates',
    'SLE-Module-Containers12-Pool',
    'SLE-Module-Containers12-Updates',
    'SLE-Module-Legacy12-Debuginfo-Pool',
    'SLE-Module-Legacy12-Debuginfo-Updates',
    'SLE-Module-Legacy12-Pool',
    'SLE-Module-Legacy12-Updates',
    'SLE-Module-Public-Cloud12-Debuginfo-Pool',
    'SLE-Module-Public-Cloud12-Debuginfo-Updates',
    'SLE-Module-Public-Cloud12-Pool',
    'SLE-Module-Public-Cloud12-Updates',
    'SLE-Module-Toolchain12-Debuginfo-Pool',
    'SLE-Module-Toolchain12-Debuginfo-Updates',
    'SLE-Module-Toolchain12-Pool',
    'SLE-Module-Toolchain12-Updates',
    'SLE-Module-Web-Scripting12-Debuginfo-Pool',
    'SLE-Module-Web-Scripting12-Debuginfo-Updates',
    'SLE-Module-Web-Scripting12-Pool',
    'SLE-Module-Web-Scripting12-Updates'
]

SLE_12_SAP = [
    'SLE12-SAP-Debuginfo-Pool',
    'SLE-12-SAP-Debuginfo-Updates',
    'SLE12-SAP-Pool',
    'SLE12-SAP-Source-Pool',
    'SLE-12-SAP-Updates',
    'SLE-HA12-Debuginfo-Pool',
    'SLE-HA12-Debuginfo-Updates',
    'SLE-HA12-Pool',
    'SLE-HA12-Source-Pool',
    'SLE-HA12-Updates'
]

SLE_12_SP1_BASE = [
    'SLES12-SP1-Debuginfo-Pool',
    'SLES12-SP1-Debuginfo-Updates',
    'SLES12-SP1-Pool',
    'SLES12-SP1-Updates',
    'SLE-SDK12-SP1-Debuginfo-Pool',
    'SLE-SDK12-SP1-Debuginfo-Updates',
    'SLE-SDK12-SP1-Pool',
    'SLE-SDK12-SP1-Updates'
]

SLE_12_SP1_MODULES = SLE_12_MODULES

SLE_12_SP1_SAP = [
    'SLE12-SP1-SAP-Debuginfo-Pool',
    'SLE-12-SP1-SAP-Debuginfo-Updates',
    'SLE12-SP1-SAP-Pool',
    'SLE12-SP1-SAP-Source-Pool',
    'SLE-12-SP1-SAP-Updates',
    'SLE-HA12-SP1-Debuginfo-Pool',
    'SLE-HA12-SP1-Debuginfo-Updates',
    'SLE-HA12-SP1-Pool',
    'SLE-HA12-SP1-Source-Pool',
    'SLE-HA12-SP1-Updates'
]

SLE_12_SP2_BASE = [
    'SLES12-SP2-Debuginfo-Pool',
    'SLES12-SP2-Debuginfo-Updates',
    'SLES12-SP2-Pool',
    'SLES12-SP2-Updates',
    'SLE-SDK12-SP2-Debuginfo-Pool',
    'SLE-SDK12-SP2-Debuginfo-Updates',
    'SLE-SDK12-SP2-Pool',
    'SLE-SDK12-SP2-Updates'
]

SLE_12_SP2_MODULES = SLE_12_SP1_MODULES + [
    'SLE-Module-HPC12-Debuginfo-Pool',
    'SLE-Module-HPC12-Debuginfo-Updates',
    'SLE-Module-HPC12-Pool',
    'SLE-Module-HPC12-Updates'
]

SLE_12_SP2_SAP = [
    'SLE12-SP2-SAP-Debuginfo-Pool',
    'SLE-12-SP2-SAP-Debuginfo-Updates',
    'SLE12-SP2-SAP-Pool',
    'SLE12-SP2-SAP-Source-Pool',
    'SLE-12-SP2-SAP-Updates',
    'SLE-HA12-SP2-Debuginfo-Pool',
    'SLE-HA12-SP2-Debuginfo-Updates',
    'SLE-HA12-SP2-Pool',
    'SLE-HA12-SP2-Source-Pool',
    'SLE-HA12-SP2-Updates'
]

SLE_12_SP3_BASE = [
    'SLES12-SP3-Debuginfo-Pool',
    'SLES12-SP3-Debuginfo-Updates',
    'SLES12-SP3-Pool',
    'SLES12-SP3-Updates',
    'SLE-SDK12-SP3-Debuginfo-Pool',
    'SLE-SDK12-SP3-Debuginfo-Updates',
    'SLE-SDK12-SP3-Pool',
    'SLE-SDK12-SP3-Updates'
]

SLE_12_SP3_MODULES = SLE_12_SP2_MODULES

SLE_12_SP3_SAP = [
    'SLE12-SP3-SAP-Debuginfo-Pool',
    'SLE-12-SP3-SAP-Debuginfo-Updates',
    'SLE12-SP3-SAP-Pool',
    'SLE12-SP3-SAP-Source-Pool',
    'SLE-12-SP3-SAP-Updates',
    'SLE-HA12-SP3-Debuginfo-Pool',
    'SLE-HA12-SP3-Debuginfo-Updates',
    'SLE-HA12-SP3-Pool',
    'SLE-HA12-SP3-Source-Pool',
    'SLE-HA12-SP3-Updates'
]

SLE_12_SP4_BASE = [
    'SLES12-SP4-Debuginfo-Pool',
    'SLES12-SP4-Debuginfo-Updates',
    'SLES12-SP4-Pool',
    'SLES12-SP4-Updates',
    'SLE-SDK12-SP4-Debuginfo-Pool',
    'SLE-SDK12-SP4-Debuginfo-Updates',
    'SLE-SDK12-SP4-Pool',
    'SLE-SDK12-SP4-Updates'
]

SLE_12_SP4_MODULES = SLE_12_SP3_MODULES

SLE_12_SP4_SAP = [
    'SLE12-SP4-SAP-Debuginfo-Pool',
    'SLE-12-SP4-SAP-Debuginfo-Updates',
    'SLE12-SP4-SAP-Pool',
    'SLE12-SP4-SAP-Source-Pool',
    'SLE-12-SP4-SAP-Updates',
    'SLE-HA12-SP4-Debuginfo-Pool',
    'SLE-HA12-SP4-Debuginfo-Updates',
    'SLE-HA12-SP4-Pool',
    'SLE-HA12-SP4-Source-Pool',
    'SLE-HA12-SP4-Updates'
]

SLE_15_BASE = [
    'SLE-Module-Basesystem15-Debuginfo-Pool',
    'SLE-Module-Basesystem15-Debuginfo-Updates',
    'SLE-Module-Basesystem15-Pool',
    'SLE-Module-Basesystem15-Updates'
]

SLE_15_PRODUCTS = [
    'SLE-Product-SLES15-Pool',
    'SLE-Product-SLES15-Updates'
]

SLE_15_MODULES = [
    'SLE-Module-CAP-Tools15-Debuginfo-Pool',
    'SLE-Module-CAP-Tools15-Debuginfo-Updates',
    'SLE-Module-CAP-Tools15-Pool',
    'SLE-Module-CAP-Tools15-Updates',
    'SLE-Module-Containers15-Debuginfo-Pool',
    'SLE-Module-Containers15-Debuginfo-Updates',
    'SLE-Module-Containers15-Pool',
    'SLE-Module-Containers15-Updates',
    'SLE-Module-Desktop-Applications15-Debuginfo-Pool',
    'SLE-Module-Desktop-Applications15-Debuginfo-Updates',
    'SLE-Module-Desktop-Applications15-Pool',
    'SLE-Module-Desktop-Applications15-Updates',
    'SLE-Module-DevTools15-Debuginfo-Pool',
    'SLE-Module-DevTools15-Debuginfo-Updates',
    'SLE-Module-DevTools15-Pool',
    'SLE-Module-DevTools15-Updates',
    'SLE-Module-Legacy15-Debuginfo-Pool',
    'SLE-Module-Legacy15-Debuginfo-Updates',
    'SLE-Module-Legacy15-Pool',
    'SLE-Module-Legacy15-Updates',
    'SLE-Module-Public-Cloud15-Debuginfo-Pool',
    'SLE-Module-Public-Cloud15-Debuginfo-Updates',
    'SLE-Module-Public-Cloud15-Pool',
    'SLE-Module-Public-Cloud15-Updates',
    'SLE-Module-Server-Applications15-Debuginfo-Pool',
    'SLE-Module-Server-Applications15-Debuginfo-Updates',
    'SLE-Module-Server-Applications15-Pool',
    'SLE-Module-Server-Applications15-Updates',
    'SLE-Module-Web-Scripting15-Debuginfo-Pool',
    'SLE-Module-Web-Scripting15-Debuginfo-Updates',
    'SLE-Module-Web-Scripting15-Pool',
    'SLE-Module-Web-Scripting15-Updates'
]

SLE_15_SAP = [
    'SLE-Module-SAP-Applications15-Debuginfo-Pool',
    'SLE-Module-SAP-Applications15-Debuginfo-Updates',
    'SLE-Module-SAP-Applications15-Pool',
    'SLE-Module-SAP-Applications15-Updates',
    'SLE-Product-HA15-Debuginfo-Pool',
    'SLE-Product-HA15-Debuginfo-Updates',
    'SLE-Product-HA15-Pool',
    'SLE-Product-HA15-Updates',
    'SLE-Product-SLES_SAP15-Debuginfo-Pool',
    'SLE-Product-SLES_SAP15-Debuginfo-Updates',
    'SLE-Product-SLES_SAP15-Pool',
    'SLE-Product-SLES_SAP15-Updates'
]

SLES_REPOS = {
    '11.4': SLE_11_SP4_BASE + SLE_11_SP4_MODULES,
    '12': SLE_12_BASE + SLE_12_MODULES,
    '12-SAP': SLE_12_SAP + SLE_12_BASE + SLE_12_MODULES,
    '12-SP1': SLE_12_SP1_BASE + SLE_12_SP1_MODULES,
    '12-SP1-SAP': SLE_12_SP1_SAP + SLE_12_SP1_BASE + SLE_12_SP1_MODULES,
    '12-SP2': SLE_12_SP2_BASE + SLE_12_SP2_MODULES,
    '12-SP2-SAP': SLE_12_SP2_SAP + SLE_12_SP2_BASE + SLE_12_SP2_MODULES,
    '12-SP3': SLE_12_SP3_BASE + SLE_12_SP3_MODULES,
    '12-SP3-SAP': SLE_12_SP3_SAP + SLE_12_SP3_BASE + SLE_12_SP3_MODULES,
    '12-SP4': SLE_12_SP4_BASE + SLE_12_SP4_MODULES,
    '12-SP4-SAP': SLE_12_SP4_SAP + SLE_12_SP4_BASE + SLE_12_SP4_MODULES,
    '15': SLE_15_BASE + SLE_15_MODULES + SLE_15_PRODUCTS,
    '15-SAP': SLE_15_SAP + SLE_15_BASE + SLE_15_MODULES
}


@pytest.fixture()
def get_sles_repos():
    def f(version):
        return SLES_REPOS[version]
    return f


@pytest.fixture()
def is_sles_sap(host):
    def f():
        sap = host.file('/etc/products.d/SLES_SAP.prod')
        return sap.exists and sap.is_file
    return f


@pytest.fixture()
def confirm_sles_license_content(host):
    def f(license_dirs):
        license_content = [
            'SUSE End User License Agreement',
            'SUSE(R) Linux Enterprise End User License Agreement',
            'SUSE® Linux Enterprise End User License Agreement'
        ]

        for license_dir in license_dirs:
            lic_dir = host.file(license_dir)

            if lic_dir.exists and lic_dir.is_directory:
                lic = host.file(license_dir + 'license.txt')
                return all([
                    lic.exists,
                    lic.is_file,
                    any(lic.contains(content) for content in license_content)
                ])

        return False
    return f
