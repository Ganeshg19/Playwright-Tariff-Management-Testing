import pytest
from playwright.sync_api import Page
import time
from datetime import datetime

class TestTariffManagementMoreBugs:
    """Additional bug validation tests (NO PAGE REFRESHES)"""
    
    def test_12_bug_alignment_issue_tariff(self, logged_in_page: Page):
        """BUG #10: Single, double, triple agree alignment not in center (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_10_alignment_issue_{timestamp}.png")
        
    def test_13_bug_tooltip_room_charge_table(self, logged_in_page: Page):
        """BUG #11: Tool tip not shown in Room charge details table (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_11_tooltip_room_charge_{timestamp}.png")
        
    def test_14_bug_to_date_captured_wrongly(self, logged_in_page: Page):
        """BUG #12: To Date captured wrongly in screen (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_12_to_date_wrong_{timestamp}.png")
        
    def test_15_bug_tariff_field_length(self, logged_in_page: Page):
        """BUG #13: Tariff fields amount able to enter more (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_13_tariff_length_{timestamp}.png")
        
    def test_16_bug_pagination_room_charge(self, logged_in_page: Page):
        """BUG #14: Remove pagination in Room charge Details (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_14_pagination_{timestamp}.png")
        
    def test_17_bug_tac_percentage_dot(self, logged_in_page: Page):
        """BUG #15: TAC Percentage dot not allowing issue (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_15_tac_percentage_dot_{timestamp}.png")
        
    def test_18_bug_date_manually_edit(self, logged_in_page: Page):
        """BUG #16: Date manually allowing to edit (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_16_date_manual_edit_{timestamp}.png")
        
    def test_19_bug_filter_not_cleared(self, logged_in_page: Page):
        """BUG #17: Filter not cleared after property name selected (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_17_filter_not_cleared_{timestamp}.png")
        
    def test_20_bug_design_overlaps(self, logged_in_page: Page):
        """BUG #18: Design overlaps on horizontal scroll (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_18_design_overlaps_{timestamp}.png")
        
    def test_21_bug_firefox_design_issue(self, logged_in_page: Page):
        """BUG #19: Design issue in Firefox browser (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_19_firefox_design_{timestamp}.png")
        
    def test_22_bug_room_image_text_issue(self, logged_in_page: Page):
        """BUG #20: Room image upload inside the box - Text issue (NO REFRESH)"""
        # No page refresh - continue on same page
        time.sleep(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logged_in_page.screenshot(path=f"assets/bugs/bug_20_room_image_text_{timestamp}.png")
