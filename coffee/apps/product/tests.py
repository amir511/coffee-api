from rest_framework import status
from rest_framework.test import APITestCase


class TestCoffeeApi(APITestCase):
    def setUp(self):
        self.API_PREFIX = "/api/v1/"
        self.machines_url = self.API_PREFIX + "machines/"
        self.pods_url = self.API_PREFIX + "pods/"

    def test_get_large_machines(self):
        params = "?product_type=large"
        res = self.client.get(self.machines_url + params)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        SKU_list = [i["SKU_number"] for i in res.data].sort()
        self.assertEqual(SKU_list, ["CM101", "CM102", "CM103"].sort())

    def test_get_large_pods(self):
        params = "?product_type=large"
        res = self.client.get(self.pods_url + params)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        SKU_list = [i["SKU_number"] for i in res.data].sort()
        self.assertEqual(
            SKU_list,
            [
                "CP101",
                "CP103",
                "CP111",
                "CP113",
                "CP121",
                "CP123",
                "CP131",
                "CP133",
                "CP141",
                "CP143",
            ].sort(),
        )

    def test_get_espresso_vanilla_pods(self):
        params = "?product_type=espresso?coffee_flavor=vanilla"
        res = self.client.get(self.pods_url + params)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        SKU_list = [i["SKU_number"] for i in res.data].sort()
        self.assertEqual(SKU_list, ["EP003", "EP005", "EP007"].sort())

    def test_get_espresso_machines(self):
        params = "?product_type=espresso"
        res = self.client.get(self.machines_url + params)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        SKU_list = [i["SKU_number"] for i in res.data].sort()
        self.assertEqual(
            SKU_list,
            [
                "EM001",
                "EM002",
                "EM003",
            ].sort(),
        )

    def test_get_small_pods(self):
        params = "?product_type=small"
        res = self.client.get(self.pods_url + params)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        SKU_list = [i["SKU_number"] for i in res.data].sort()
        self.assertEqual(
            SKU_list,
            [
                "CP003",
                "CP011",
                "CP013",
                "CP021",
                "CP023",
                "CP031",
                "CP033",
                "CP041",
                "CP043",
            ].sort(),
        )

    def test_get_seven_dozen_pods(self):
        params = "?pack_size=7"
        res = self.client.get(self.pods_url + params)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        SKU_list = [i["SKU_number"] for i in res.data].sort()
        self.assertEqual(
            SKU_list,
            [
                "EP007",
                "EP017",
            ].sort(),
        )
