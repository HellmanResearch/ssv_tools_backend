
import os
import json
import logging
import datetime
import subprocess
from django.conf import settings

from . import random as l_random

logger = logging.getLogger(__name__)


class DepositKey:

    key_base_dir = os.path.join(settings.BASE_DIR, "deposit_keys")

    # def __init__(self):
    #     self.id = None
    #     # key_dir = os.path.join(self.key_base_dir, str(id))
    #     # if os.path.exists(key_dir):
    #     #     raise Exception(f"{key_dir} has exist")
    #     # os.makedirs(self.script_dir)

    def __init__(self, key_dir):
        self.key_dir = key_dir
        # dir_name = l_random.get_dir_name()
        # self.dir_name = "deposit_" + dir_name
        # self.key_dir = os.path.join(self.key_base_dir, self.dir_name)
        self.deposit_file_path = os.path.join(settings.BASE_DIR, "eth2.0-deposit-cli/eth2deposit/deposit.py")
        self.deposit_project_path = os.path.join(settings.BASE_DIR, "eth2.0-deposit-cli")
        self.full_path = os.path.join(self.key_base_dir, self.key_dir)

    def create(self):
        if os.path.exists(self.full_path):
            raise Exception(f"{self.full_path} has exist")
        os.makedirs(self.full_path)
        password = l_random.get_password()
        cmd = f"cd {self.deposit_project_path}; python3 {self.deposit_file_path} new-mnemonic --num_validators 1 --chain prater --keystore_password {password}1 --folder {self.full_path}"
        self.run_cmd(cmd, timeout=20)
        hex_data = self.get_hex()
        with open(f"{self.full_path}/validator_keys/hex_data.txt", "w") as f:
            f.write(hex_data)

    def get_hex(self):
        # deposit_file_path = sys.argv[1]
        validator_keys_path = os.path.join(self.full_path, "validator_keys")
        file_name_list = os.listdir(validator_keys_path)
        deposit_file_name_list = [item for item in file_name_list if item.startswith("deposit_data-")]
        if len(deposit_file_name_list) != 1:
            raise Exception(f"key dir has {len(deposit_file_name_list)} deposit files")
        file_path = os.path.join(validator_keys_path, deposit_file_name_list[0])
        with open(file_path) as f:
            content = f.read()

        body_1 = "0x22895118000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000e00000000000000000000000000000000000000000000000000000000000000120"
        body_2 = "0000000000000000000000000000000000000000000000000000000000000030"
        body_3 = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020"
        body_4 = "0000000000000000000000000000000000000000000000000000000000000060"

        deposit_data = json.loads(content)
        deposit_data_length = len(deposit_data)
        if deposit_data_length != 1:
            raise Exception(f"deposit file content has {deposit_data_length} item")
        item = deposit_data[0]
        hex = f"{body_1}{item['deposit_data_root']}{body_2}{item['pubkey']}{body_3}{item['withdrawal_credentials']}{body_4}{item['signature']}"
        return hex

    def get_zip_file_path(self):
        return self.full_path + ".zip"

    def get_zip_file_name(self):
        return self.key_dir + ".zip"

    def create_zip(self):
        zip_file_name = self.get_zip_file_name()
        zip_file_path = self.get_zip_file_path()
        cmd = f"cd {self.key_base_dir};zip -r {zip_file_name} {self.key_dir}"
        self.run_cmd(cmd, timeout=10)
        return zip_file_path

    def run_cmd(self, cmd, timeout=30):
        env = os.environ.copy()
        env["PYTHONPATH"] = self.deposit_project_path
        try:
            cp = subprocess.run(cmd, shell=True, encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                timeout=timeout, env=env)
        except subprocess.TimeoutExpired as exc:
            err_msg = f"timeout ({timeout}s)"
            logger.debug(err_msg)
            raise exc
        if cp.returncode != 0:
            err_msg = f"run cmd: {cmd} failed, stdout: {cp.stdout} stderr: {cp.stderr}"
            logger.debug(err_msg)
            raise Exception(err_msg)
        return cp.stdout

