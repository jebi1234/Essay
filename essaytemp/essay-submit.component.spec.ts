import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EssaySubmitComponent } from './essay-submit.component';

describe('EssaySubmitComponent', () => {
  let component: EssaySubmitComponent;
  let fixture: ComponentFixture<EssaySubmitComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EssaySubmitComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EssaySubmitComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
