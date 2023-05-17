#################### PACKAGE ACTIONS ###################

reinstall_package:
	@pip uninstall -y emosense || :
	@pip install -e .

##################### TESTS #####################
default:
	PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -v --color=yes

# test_app: test_interface \
# 	test_ml_logic

# test_interface:
# 	@pytest \
# 	tests/interface/test_console_app.py \
# 	tests/interface/test_api.py \
# 	tests/interface/test_api.py::TestPred::test_pred_from_url_1 \
# 	tests/interface/test_api.py::TestPred::test_pred_from_url_2
