credit_report = """
# Credit Report Summary

**Report Details:**
- Enquiry Control Number: 3916175359
- Member Reference: ANG250707490564801
- Report Date: 2025-05-31

---

## Loan Account 1: Housing Loan

**Basic Information:**
- Loan Type: Housing Loan
- Loan Status: Live (Active)
- Ownership: Joint
- Date Opened: 2025-05-26
- Last Payment: 2025-05-26

**Financial Details:**
- Sanctioned Amount: ₹1,71,58,388
- Outstanding Balance: ₹62,30,341
- Loan Classification: Standard (0)
- Write-off Amount: ₹0

**Borrower Profile:**
- Monthly Gross Income: ₹4,66,617
- Occupation Code: 1
- Payment History Period: May 2025

---

## Loan Account 2: Personal Loan

**Basic Information:**
- Loan Type: Personal Loan
- Loan Status: Live (Active)
- Ownership: Individual
- Date Opened: 2025-04-03
- Last Payment: 2025-05-05

**Financial Details:**
- Sanctioned Amount: ₹20,00,000
- Outstanding Balance: ₹19,75,927
- EMI Amount: ₹43,362
- Loan Tenure: 60 months
- Tenor Frequency: Quarterly (3)
- Loan Classification: Standard (0)
- Write-off Amount: ₹0

**Payment History:**
- Payment History Period: April-May 2025

---
"""
bank_statement = """
# Bank Transaction Data - April & May 2025 (Compressed)

## April 2025 - Credits (₹3,967,453.27)

| Date | Amount (₹) | Type | Description |
|------|------------|------|-------------|
| 2025-04-02,06,23 | 16 | Loan | Navi Finance transfers |
| 2025-04-02 | 121 | Interest | Angel Broking payment |
| 2025-04-11 | 90,000 | Transfer | From Andey Lakshmi D |
| 2025-04-03 | 1,471,606.18 | Internal | ICICI/CMS transfer + penny drop |
| 2025-04-05 | 3,941.09 | Internal | Groww withdrawal |
| 2025-04-07,08,10 | 10,701 | Internal | PayLater/Angel One/Kotak transfers |
| 2025-04-21 | 1,000,000 | Internal | RTGS from Kotak Mahindra (2 transfers) |
| 2025-04-30 | 300,000 | Internal | RTGS from Basavayya Chowdary |
| 2025-04-25 | 10,000 | UPI | Saidulu Anupati |
| 2025-04-26 | 90,000 | UPI | VK Kishore (SBI) - 2 payments |
| 2025-04-27 | 90,000 | UPI | Lakshmi Naidu (Axis) |
| 2025-04-28 | 30,000 | UPI | VK Kishore (SBI) |
| 2025-04-29 | 90,000 | UPI | VK Kishore (SBI) - 2 payments |
| 2025-04-30 | 180,000 | UPI | YBL/VK Kishore (Axis/ICICI) - 3 payments |
| 2025-04-29 | 649,969 | Salary | Angel One Limited |

## April 2025 - Debits (₹2,461,261.82)

| Date | Amount (₹) | Type | Description |
|------|------------|------|-------------|
| 2025-04-01 | 1,334 | UPI | BOB/Cashfree/Verce/Airtel/Yes Bank payments |
| 2025-04-04 | 1,000,000 | Bill | Bajaj Finance |
| 2025-04-21 | 993,207 | Bill | Tata Capital + Chigurupati Kal |
| 2025-04-28 | 2,358.82 | Bill | NoBroker |
| 2025-04-06,29,30 | 397,000 | Internal | Kotak (260k) + Standard Chartered (137k) |
| 2025-04-25 | 10,000 | Cash | ATM Hyderabad |
| 2025-04-02 | 43,362 | Loan EMI | Personal loan |
| 2025-04-16,20 | 15,000 | Investment | Groww stock purchases |

## May 2025 - Credits (₹774,869.50)

| Date | Amount (₹) | Type | Description |
|------|------------|------|-------------|
| 2025-05-02 | 41,350 | UPI | Maya Manvi/VK Kishore/Kaleru Sandeep |
| 2025-05-18 | 1,100 | UPI | Amazon Pay reload |
| 2025-05-03,06,07,08,10,19,20 | 245,700 | Internal | Kotak Mahindra + Angel One transfers |
| 2025-05-17 | 1 | Loan | Navi Finance |
| 2025-05-20,30 | 7,579.50 | Other | SBI reversal + interest |
| 2025-05-28 | 479,139 | Salary | Angel One Limited |

## May 2025 - Debits (₹600,020.30)

| Date | Amount (₹) | Type | Description |
|------|------------|------|-------------|
| 2025-05-01,05 | 45,708 | UPI | SBI/IDBI/Loan EMI/Airtel payments |
| 2025-05-01 | 310,275 | Bill | SAS IT Tower (2 payments) |
| 2025-05-26,30 | 4,790.30 | Bill | IRCTC tickets |
| 2025-05-04 | 2,247 | Loan EMI | ACH via Razorpay |
| 2025-05-28 | 237,000 | Internal | Standard Chartered (137k) + Kotak (100k) |

## Summary

| Month | Credits (₹) | Debits (₹) | Net (₹) |
|-------|-------------|------------|---------|
| April | 3,967,453 | 2,461,262 | +1,506,191 |
| May | 774,870 | 600,020 | +174,850 |

"""

pay_slip = """
# Employee Payslip - April 2025

## Employee Information
- **Name**: MANIKANTA DINESH VAKAMUDI
- **Employee Code**: E89371
- **Designation**: DEPUTY VICE PRESIDENT
- **Department**: SALES
- **Location**: BENGALURU-BELLANDUR
- **Date of Joining**: 14/Nov/2024
- **Date of Birth**: 04/Aug/1990
- **PAN**: ASBPV0118P
- **Bank**: ICICI BANK (Account: 142001515109)
- **Tax Regime**: OLD

## Attendance Summary
- **Calendar Days**: 30
- **Present Days**: 30
- **Absent Days**: 0
- **Arrear Days**: 0

## Salary Breakdown

### Earnings
| Component | Monthly Rate (₹) | Current Month (₹) | Arrears (₹) | Total (₹) |
|-----------|------------------|-------------------|-------------|-----------|
| Basic | 249,347 | 249,347 | 0 | 249,347 |
| HRA | 124,674 | 124,674 | 0 | 124,674 |
| Leave Travel Allowance | 8,333 | 8,333 | 0 | 8,333 |
| Special Allowance | 194,213 | 194,213 | 0 | 194,213 |
| Telephone Allowance | 2,500 | 2,500 | 0 | 2,500 |
| Professional Development Assistance | 12,000 | 12,000 | 0 | 12,000 |
| Use of Movable Assets | 15,000 | 15,000 | 0 | 15,000 |
| Mobile Handset Reimbursement | 10,000 | 10,000 | 0 | 10,000 |
| Health & Other Club Facilities | 3,000 | 3,000 | 0 | 3,000 |
| **One Time Bonus** | 0 | 0 | **224,192** | **224,192** |
| **ASM 2025 Winner Reward** | 0 | 0 | **50,000** | **50,000** |
| **GROSS EARNINGS** | **619,067** | **619,067** | **274,192** | **893,259** |

### Deductions
| Component | Amount (₹) |
|-----------|------------|
| Profession Tax | 200 |
| Income Tax | 235,690 |
| Statutory PF | 1,800 |
| Top-up Mediclaim | 800 |
| Senior Parental Medical | 4,800 |
| **TOTAL DEDUCTIONS** | **243,290** |

### Benefits in Kind
| Component | Amount (₹) |
|-----------|------------|
| Sodexo | 2,500 |
| Group Mediclaim | 1,680 |
| Group Total Protection Insurance | 750 |
| **TOTAL BENEFITS** | **4,930** |

## Salary Summary
- **Earned Gross (A + C)**: ₹8,98,189
- **Net Salary (A - B)**: ₹6,49,969
- **In Words**: Six Lakh Forty Nine Thousand Nine Hundred Sixty Nine Only

## Annual Tax Calculation Summary

### Income Components
- **Annual Salary**: ₹77,02,996
- **Less: Deductions U/s 10**: ₹14,10,784
- **Income Subtotal**: ₹62,92,212
- **Less: Standard Deduction**: ₹50,000
- **Less: Employment Tax**: ₹2,500
- **Less: Other Income**: ₹2,00,000
- **Less: Mediclaim**: ₹39,948
- **Less: Investment U/s 80C**: ₹1,50,000
- **Total Taxable Income**: ₹58,49,770

### Tax Calculation
| Income Slab | Tax Rate | Tax Amount |
|-------------|----------|------------|
| ₹0 - ₹2,50,000 | 0% | ₹0 |
| ₹2,50,001 - ₹5,00,000 | 5% | ₹12,500 |
| ₹5,00,001 - ₹10,00,000 | 20% | ₹1,00,000 |
| ₹10,00,001 - ₹50,00,000 | 30% | ₹12,00,000 |
| ₹50,00,001 - ₹1,00,00,000 | 30% | ₹2,54,931 |
| **Base Tax** | | **₹15,67,431** |
| **Surcharge (10%)** | | **₹1,56,743** |
| **Health & Education Cess (4%)** | | **₹68,967** |
| **Total Tax Payable** | | **₹17,93,141** |

### Section 10 Exemptions
| Component | Exempted Amount (₹) |
|-----------|---------------------|
| Telephone Allowance | 30,000 |
| Mobile Handset Reimbursement | 1,20,000 |
| Health & Other Club Facilities | 36,000 |
| Use of Movable Assets | 1,80,000 |
| Professional Development Assistance | 9,00,784 |
| HRA (Rent: ₹1,00,000 p.m. for 12 months) | To be calculated |

## Tax Information
- **Tax for April 2025**: ₹2,35,690
- **Remaining Tax to be Deducted**: ₹15,57,451
"""