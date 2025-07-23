json_string = """
{
  "April": {
    "credits": {
      "salary_credit": [
        {
          "transaction_date": "2025-04-02",
          "amount": 121.00,
          "narration": "Salary from Angel One",
          "month_bucket": "1-7",
          "balance": 71836.20
        },
        {
          "transaction_date": "2025-04-08",
          "amount": null,
          "narration": "Salary from Angel One",
          "month_bucket": "8-14",
          "balance": null
        },
        {
          "transaction_date": "2025-04-29",
          "amount": 649969.00,
          "narration": "Salary from Angel One",
          "month_bucket": "22-EOM",
          "balance": 876176.89
        }
      ]
    }
  },
  "May": {
    "credits": {
      "salary_credit": [
        {
          "transaction_date": "2025-05-08",
          "amount": 700.00,
          "narration": "Salary from Angel One",
          "month_bucket": "8-14",
          "balance": 6871.29
        },
        {
          "transaction_date": "2025-05-28",
          "amount": 479139.00,
          "narration": "Salary from Angel One",
          "month_bucket": "22-EOM",
          "balance": 482442.08
        }
      ],
      "loan_amount_credit": [
        {
          "transaction_date": "05-05-2025",
          "amount": 43362.00,
          "narration": "EMI",
          "month_bucket": "1-7",
          "balance": 31216.29
        }
      ]
    }
  },
  "June": {
    "credits": {
      "salary_credit": [
        {
          "transaction_date": "2025-06-06",
          "amount": 700.00,
          "narration": "Salary from Angel One",
          "month_bucket": "1-7",
          "balance": 52629.35
        },
        {
          "transaction_date": "2025-06-27",
          "amount": null,
          "narration": "Salary from Angel One",
          "month_bucket": "22-EOM",
          "balance": null
        }
      ],
      "loan_amount_credit": [
        {
          "transaction_date": "05-06-2025",
          "amount": 43362.00,
          "narration": "EMI",
          "month_bucket": "1-7",
          "balance": 60189.63
        }
      ]
    }
  }
}
"""

clssify_prompt="""
Analyze these bank transactions and classify each into EXACTLY ONE of these categories:

CREDIT CATEGORIES:
1. salary_credit - Salary deposits from employer
2. loan_amount_credit - Loan disbursements
3. internal_transfer - Transfers between own accounts
4. upi_received - UPI payments received
5. interest_credit - Interest payments from bank
6. other_credits - Any other credit transaction

DEBIT CATEGORIES:
1. emi_payments - Loan EMI payments
2. utility_payments - Electricity/phone bills etc
3. internal_transfer - Transfers between own accounts
4. upi_payments - UPI payments sent
5. charges - Bank fees/penalties
6. other_debits - Any other debit transaction

For each transaction:
- Identify transaction type (credit/debit)
- Select the most specific category possible
- Include all original transaction details
- Format amounts as pure numbers (remove commas)

Output as a list of dictionaries with keys:
transaction_date, amount, narration, transaction_type, category
"""

md_string = """
Page 1 of 28

![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

MR. MANIKANTA DINESH VAKAMUDI A607, NECKLACE PRIDE, 6, 6-6-8/32, KAVADIGUDA MAINROAD, SECUNDERABAD, NEW BHOIGUDA HYDERABAD TELANGANA - INDIA - 500003

Your Base Branch: G-1, NAVKETAN, 62, SD ROAD, OPP CLOCK TOWER, 500003

Visit www.icicibank.com Dial your Bank 7306667777

Did you know? It's mandatory to be KYC compliant as per RBI guidelines. If you have not submitted your KYC documents, please visit the nearest branch or contact your Relationship Manager to complete KYC details for your Account.

Summary of Accounts held under Cust ID: 531539419 as on July 13, 2025

ACCOUNT DETAILS - INR

|  ACCOUNT TYPE | A/c BALANCE(1) | FIXED DEPOSITS (LINKED) BAL (1) | TOTAL BALANCE(1+1) | NOMINATION  |
| --- | --- | --- | --- | --- |
|  Savings A/c 142001515109 | 14,246.15 | 0.00 | 14,246.15 | Registered  |
|  TOTAL | 14,246.15 | 0.00 | 14,246.15 |   |

Statement of Transactions in Savings Account Number: 142001515109 in INR for the period April 01, 2025 - July 13, 2025

|  DATE | MODE** | CERTIFICATE | DEPOSITS | VOTING BALANCE | BALANCE  |
| --- | --- | --- | --- | --- | --- |
|  01-04-2025 |  | B/F |  |  | 73,035.20  |
|   |  | UPI/8184979046-3@yb/na/BANK OF BARODA/509122713188/ICIWC8C921AF7E47FE2E1 DB690694F6663B/ |  | 500.00 | 72,535.20  |
|  01-04-2025 |  | UPI/cf.frnd12@cashf/Payment from Ph/NSDL PAYMENTSB/646803068985/AXL24663960f307415 6b856775bde7f44ba |  | 664.00 | 71,871.20  |
|  01-04-2025 |  | UPI/cfvercesolution/Payment for ord/YES BANK LIMITE/656211203628/AXL4f2451d13e9f4c8db31ae b832ecc6ab3 |  | 30.00 | 71,841.20  |
|  01-04-2025 |  | UPI/9956377955@ybl/Payment from Ph/AIRTEL PAYMENTS/396863646961/YBL67dcc40ee2f24d9aa 29fd4efb28bff5f/ |  | 40.00 | 71,801.20  |
|  01-04-2025 |  | UPI/cfvercesolution/Payment for ord/YES BANK LIMITE/103187871478/AXLae47fcf672c3437f8b7fce b6542bbdde |  | 80.00 | 71,721.20  |
|  01-04-2025 |  | UPI/Q476574543@ybl/Payment from Ph/YES BANK LIMITE/611152940772/YBLaf10eaf55b5d4252a0cd4 a7da804324f/ |  | 20.00 | 71,701.20  |
|  02-04-2025 | MOBILE BANKING | MMT/IMPS/509206346731/Fund transfer from Navi 250402IC367/Navi Finse to MANIKANTA | 14.00 |  | 71,715.20  |
|  02-04-2025 |  | ACH/ANGEL Int2 2024 25/292815 | 121.00 |  | 71,836.20  |
|  02-04-2025 |  | UPI/Vyapar.17214179/Payment from Ph/HDFC BANK LTD/161013933750/AXL76f974a964344cbca7ebbb1 97b93c0ff/ |  | 355.00 | 71,481.20  |
|  02-04-2025 |  | UPI/netflixupi.payu/Monthly autopay/HDFC BANK LTD/100283267798/HDF310E52DBC9B2E60FE0634 ECEE10AFC4E/ |  | 649.00 | 70,832.20  |
|  02-04-2025 |  | UPI/frnd522.rzp@ici/Payment from Ph/ICICI Bank LTD /594989020819/YBL4e415ce17b9c4a1e91eeabb527 355ac7 |  | 664.00 | 70,168.20  |
|  02-04-2025 |  | UPI/bhukyabixapathi/Payment from Ph/BANK OF BARODA/139693221579/AXL54429ed78a794fdaaeb 715b53d03ac8f/ |  | 130.00 | 70,038.20  |
|  02-04-2025 |  | UPI/paytmg/28100505/Payment from Ph/YES BANK LIMITE/503060487524/AXL768b4a71c7e24610952fd 07cf46f41b5 |  | 440.00 | 69,598.20  |

---

# 9iciciBank khayaal aapka

MR.MANIKANTA DINESH VAKAMUDI

|  DATE | MODE ${ }^{\text {a }}$ | PARTICULARS | DEPOSITS | WITHDRAWALS | BALANCE  |
| --- | --- | --- | --- | --- | --- |
|  02-04-2025 |  | UPI/Vyapar.17214179/Payment from Ph/HDFC BANK |  | 239.00 | 69,359.20  |
|   |  | LTD/157004532337/AXL2ad258948f8245cebd7e564 a61fcd829/ |  |  |   |
|  02-04-2025 |  | UPI/paytmq28100505/Payment from Ph/YES BANK |  | 40.00 | 69,319.20  |
|   |  | LIMITE/416527246248/YBL86c59a4133584fc4a813a 3afc1b1fdf1 |  |  |   |
|  03-04-2025 | MOBILE BANKING | MMT/IMPS/509314665028/iciciBankCredit/PERFIOS SO/IDFC bank | 1.00 |  | 69,320.20  |
|  03-04-2025 | CMS TRANSACTION | CMS/
LPHYD00050999086C1353966585MANIKANTA DINE147 | $14,71,605.18$ |  | 15,40,925.38  |
|  03-04-2025 |  | BIL/ONL/000992813781/NAVI
FINSE/QEXFLVYCPKKW61 |  | 5,04,477.00 | 10,36,448.38  |
|   |  | UPI/frnd522.rzp@ici/Payment from Ph/ICICI Bank |  |  |   |
|  03-04-2025 |  | LTD
/459174399358/AXL5ce3a3f6fb1f4500ba27d8e08e0f b157 |  | 664.00 | 10,35,784.38  |
|   |  | UPI/paytm.s15mz0s@p/Payment from Ph/YES BANK |  |  |   |
|  03-04-2025 |  | PTY/035287377153/AXLa5f9d17b558a485298b5d18 a2f7c9398/ |  | 40.00 | 10,35,744.38  |
|   |  | UPI/tataaialif.bdsi/MandateRequest/ICICI Bank |  |  |   |
|  03-04-2025 |  | LTD/509337005473/ICIbf12519762d341e9bc5855ad 7c09ef9a/ |  | 9,029.00 | 10,26,715.38  |
|   |  | UPI/navi.insurance2/Upi Mandate/ICICI Bank LTD /509437653753/ICI056a123b12ff40579dd1acf063b41 6d3/ |  | 1,241.46 | 10,25,473.92  |
|  04-04-2025 |  | ACH/CTRAZORPAY/ICIC7010101210004472/ICICIPR UDEQEUVvm5G1FFnz |  | 2,247.00 | 10,23,226.92  |
|   |  | UPI/razorpay.2@icic/Pay via Razorpa/ICICI Bank |  |  |   |
|  04-04-2025 |  | LTD
/509438649417/ICla76bd88d60e048a9acd38df15033 b06e |  | 235.00 | 10,22,991.92  |
|  04-04-2025 |  | BIL/ONL/000993220253/Bajaj Fina/httpswwwbajajfi |  | 10,00,000.00 | 22,991.92  |
|  04-04-2025 |  | UPI/Q822873715@ybl/Payment from Ph/YES BANK |  | 2,500.00 | 20,491.92  |
|   |  | LIMITE/130709702024/YBLe15a14a4edde45c4a2de ee4e6f0a00d8/ |  |  |   |
|  04-04-2025 |  | UPI/cred.club@axisb/payment on CRED/AXIS BANK/546064354393/ACD3099307250pWbgZRw/ |  | 1.26 | 20,490.66  |
|  05-04-2025 | CMS TRANSACTION | CMS/ GROWW WITHDRAW REQ MANIKANTA DINESH VAK/NEXT | 3,941.09 |  | 24,431.75  |
|  05-04-2025 |  | UPI/9021670009@ybl/Payment from Ph/Kotak |  |  |   |
|   |  | Mahindra/669685101825/YBLfadf6f3827224fdfafb78 b1492d7d91d | 50,000.00 |  | 74,431.75  |
|  05-04-2025 |  | UPI/9470198935@okbi/Payment from Ph/AXIS |  |  |   |
|   |  | BANK/279522629003/YBL5982a2cf711b441c8f4db6 9039520739/ |  | 35.00 | 74,396.75  |
|  05-04-2025 |  | UPI/9951539580@okbi/Payment from Ph/AXIS |  |  |   |
|   |  | BANK/172484231961/YBL13781e319ecf40f4ab0212 18027ef549/ |  | 104.00 | 74,292.75  |
|  05-04-2025 |  | UPI/9573647299@ybl/Payment from Ph/IDBI |  |  |   |
|   |  | BANK/211750668848/YBL9788cb7b297c4d22bcd3a a9378b05058/ |  | 40.00 | 74,252.75  |
|  05-04-2025 |  | UPI/Mswipe.25000522/Payment from Ph/Kotak |  |  |   |
|   |  | Mahindra
/807502365113/AXL5721f7027304477d93a5af3ab2c 718f2 |  | 100.00 | 74,152.75  |
|  05-04-2025 |  | UPI/9967109849@ybl/Payment from Ph/UCO |  |  |   |
|   |  | BANK/181345582349/YBL999bede5e13e480aadbad f339c767fab/ |  | 92.00 | 74,060.75  |
|  05-04-2025 |  | UPI/cfvercesolution/Payment for ord/YES BANK |  |  |   |
|   |  | LIMITE/229129055746/AXL82d45537bf734b4983e4 e5a32112d61c |  | 30.00 | 74,030.75  |
|  05-04-2025 |  | UPI/Q733355005@ybl/Payment from Ph/YES BANK |  |  |   |
|   |  | LIMITE/533355178608/YBL76905889b0254c6d9f955 c2962bd7c1b/ |  | 20.00 | 74,010.75  |

---

# 9iciciBank khayaal aapka

MR.MANIKANTA DINESH VAKAMUDI

|  DATE | MODE ${ }^{1,2}$ | PARTICULARS | DEPOSITS | WITHDRAWALS | BALANCE  |
| --- | --- | --- | --- | --- | --- |
|  05-04-2025 |  | UPI/cfvercesolution/Payment for ord/YES BANK |  | 40.00 | 73,970.75  |
|   |  | LIMITE/109952281374/AXLa77ff10f01604025ba5236 00fa210a0e |  |  |   |
|  06-04-2025 | MOBILE BANKING | MMT/IMPS/509608745413/MANIKANTA /KKBK0007466 |  | 60,000.00 | 13,970.75  |
|  06-04-2025 | MOBILE BANKING | MMT/IMPS/509609805354/Fund transfer from Navi 250406IC380/Navi Finse to MANIKANTA | 1.00 |  | 13,971.75  |
|  06-04-2025 |  | UPI/gpay-1124452836/Payment from Ph/AXIS |  | 100.00 | 13,871.75  |
|   |  | BANK/334991502057/YBLd45291151c7643a7aecb1 611d89ced87/ |  |  |   |
|  06-04-2025 |  | UPI/Q733355005@ybl/Payment from Ph/YES BANK |  | 20.00 | 13,851.75  |
|   |  | LIMITE/557319502743/YBL326dd1b48d084d31a78d 80ea537af2f1/ |  |  |   |
|  06-04-2025 |  | UPI/cf.vercesolutio/Payment for ord/ICICI Bank LTD /377985938002/YBL7a45648c69d8467eae8be45db9 868c2b |  | 35.00 | 13,816.75  |
|  06-04-2025 |  | UPI/cf.vercesolutio/Payment for ord/ICICI Bank LTD /630155266388/YBL2b287a2c32794aa2b4bd022a7ff a15ab |  | 70.00 | 13,746.75  |
|  07-04-2025 |  | UPI/jarpulavenky2@y/Payment from Ph/HDFC BANK |  | 900.00 | 12,846.75  |
|   |  | LTD/516943639274/AXL0c49850d352d4b7e9797c3 b135014e98/ |  |  |   |
|  07-04-2025 |  | UPI/paytmqr58zco4@p/Payment from Ph/YES BANK |  | 108.00 | 12,738.75  |
|   |  | LIMITE/953920433805/AXL3055f7ff091541f5abc3c3 00e7a546dd |  |  |   |
|  07-04-2025 |  | UPI/Q192959037@ybl/Payment from Ph/YES BANK |  | 35.00 | 12,703.75  |
|   |  | LIMITE/818466817232/YBLc317dea46a734c4ba4464 69d9b8c27c6/ |  |  |   |
|  07-04-2025 | MOBILE BANKING | MMT/IMPS/509715570087/P2AMOB/PL PENNY D/Indusind Bank | 1.00 |  | 12,704.75  |
|  07-04-2025 |  | UPI/paytmqr58zco4@p/Payment from Ph/YES BANK |  | 30.00 | 12,674.75  |
|   |  | LIMITE/573398950823/YBL51bd341e6d9849b6aae7 767408fdbe53 |  |  |   |
|  07-04-2025 |  | UPI/Q752835976@ybl/Payment from Ph/YES BANK |  | 30.00 | 12,644.75  |
|   |  | LIMITE/541227814943/YBLbed3d51a391c4f62a99fe f d202581758/ |  |  |   |
|  07-04-2025 |  | UPI/pal311823@okaxi/Payment from Ph/Punjab National/454467246679/AXLb4700059a46a43fd8fb9 07f04d508f83 |  | 75.00 | 12,569.75  |
|  07-04-2025 |  | UPI/7709889457@ptax/Payment from Ph/HDFC BANK |  | 1,999.00 | 10,570.75  |
|   |  | LTD/631632172416/AXL835d6b77479343e3bfb12d2 aa41a5afd/ |  |  |   |
|  07-04-2025 |  | UPI/9136184677@axl/Payment from Ph/INDIA POST |  | 2,000.00 | 8,570.75  |
|   |  | PAYM/811430486595/AXL8408352722724783941de a661d63875c/ |  |  |   |
|  07-04-2025 |  | UPI/ashishyadav5869/Payment from Ph/AXIS |  | 75.00 | 8,495.75  |
|   |  | BANK/747443154598/YBL3fd92dd7fafe4ae5bcdd7d a4e9020a37/ |  |  |   |
|  07-04-2025 |  | UPI/cf.fmd12@cashf/Payment from Ph/NSDL |  | 664.00 | 7,831.75  |
|   |  | PAYMENTSB/589721054018/YBLeaa1c3f596234ef3 b44e27442d4f1658 |  |  |   |
|  08-04-2025 |  | NEFT-HDFCN52025040866831657-ANGEL ONE |  |  |   |
|   |  | LIMITED PROPRIETARY AC-0001-15770340000330HDFC0000240 | 700.00 |  | 8,531.75  |
|  08-04-2025 |  | UPI/saybudhotre51-1/Payment from Ph/CENTRAL BANK |  | 170.00 | 8,361.75  |
|   |  | OF/554419927027/YBL62f58bb4c7504ae0b7f15afb8 2b63a35 |  |  |   |
|  08-04-2025 |  | UPI/airtelcommonpoo/Payment from Ai/AIRTEL PAYMENTS/509817971266/APB1450FmMS04MTg3 LTF/YjIwYzZmNjE5MQ |  | 1,354.64 | 7,007.11  |

"""

md_to_json_prompt = """"
I have a markdown table that I want to convert into JSON. Based on the give schema and data, output the final JSON:
JSON Schema:
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "DATE": { "type": ["string", "null"] },
      "MODE": { "type": ["string", "null"] },
      "CERTIFICATE": { "type": "string" },
      "DEPOSITS": { "type": ["number", "null"] },
      "WITHDRAWLS": { "type": ["number", "null"] },
      "BALANCE": { "type": "number" }
    },
    "required": ["DATE", "CERTIFICATE", "BALANCE"]
  }
}
Keep in mind that the certifate column has text overflow. Sometimes this column is named as particulars.
Markdown table:
|  DATE | MODE ${ }^{\text {a }}$ | PARTICULARS | DEPOSITS | WITHDRAWALS | BALANCE  |
| --- | --- | --- | --- | --- | --- |
|  02-04-2025 |  | UPI/Vyapar.17214179/Payment from Ph/HDFC BANK |  | 239.00 | 69,359.20  |
|   |  | LTD/157004532337/AXL2ad258948f8245cebd7e564 a61fcd829/ |  |  |   |
|  02-04-2025 |  | UPI/paytmq28100505/Payment from Ph/YES BANK |  | 40.00 | 69,319.20  |

"""